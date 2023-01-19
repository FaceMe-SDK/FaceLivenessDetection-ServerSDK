#include <opencv2/opencv.hpp>
#include "faceme_liveness.h"

#define LICENSE_KEY "XXXXX-XXXXX-XXXXX-XXXXX"		// Please request license to support@faceme.tw

void printUsage(const std::string& message = "");
bool parseArgs(int argc, char *argv[], std::map<std::string, std::string >& values);

int main(int argc, char *argv[]) {
    std::string modelFolder, imagePath;
   
    // Parsing args
	std::map<std::string, std::string > args;
	if (!parseArgs(argc, argv, args)) {
		printUsage();
		return -1;
	}
	if (args.find("--image") == args.end()) {
		printUsage("--image required");
		return -1;
	}
	if (args.find("--model") == args.end()) {
		printUsage("--model required");
		return -1;
	}
	imagePath = args["--image"];
    modelFolder = args["--model"];

    const char* version = fml_version();
    printf("version: %s\n", version);

    int ret = fml_init(modelFolder.c_str(), LICENSE_KEY);
    if(ret != 0) {
        printf("init failed: %d\n", ret);
        return -1;
    }

    cv::Mat image = cv::imread(imagePath);
    if(image.empty())
    {
        printf("image is null!\n");
        return -1;
    }

    int faceRect[4] = { 0 };
    double livenessScore = { 0 };
    
    ret = fml_detect_face(image.data, image.cols, image.rows, faceRect, &livenessScore);
    if(ret == -1) {
        printf("license error!\n");
    } else if(ret == -2) {
        printf("init error!\n");
    } else if(ret == 0) {
        printf("no face detected!\n");
    } else if(ret > 1) {
        printf("multiple face detected!\n");
    } else if(livenessScore > 0.5) {
        printf("genuine -> face rect %d, %d, %d, %d, liveness score = %f\n", faceRect[0], faceRect[1], faceRect[2], faceRect[3], livenessScore);
    } else {
        printf("spoof -> face rect %d, %d, %d, %d, liveness score = %f\n", faceRect[0], faceRect[1], faceRect[2], faceRect[3], livenessScore);
    }

    return 0;
}

void printUsage(const std::string& message)
{
	if (!message.empty()) {
		printf("%s", message.c_str());
	}

	printf(
		"\n********************************************************************************\n"
		"example_liveness\n"
		"\t--image <path-to-image> \n"
		"\t--model <path-to-model-folder> \n"
		"\n"
		"--image: Path to an image(JPEG/PNG/BMP).\n\n"
		"--model: Path to the folder containing models.\n\n"
        "./example_liveness --image ../../test_image/spoof.png --model ../../model\n"
		"********************************************************************************\n"
	);
}

bool parseArgs(int argc, char *argv[], std::map<std::string, std::string >& values)
{
	assert(argc > 0 && argv != nullptr);

	values.clear();

	// Make sure the number of arguments is even
	if ((argc - 1) & 1) {
		printf("Number of args must be even");
		return false;
	}

	// Parsing
	for (int index = 1; index < argc; index += 2) {
		std::string key = argv[index];
		if (key.size() < 2 || key[0] != '-' || key[1] != '-') {
			printf("Invalid key: %s", key.c_str());
			return false;
		}
		values[key] = argv[index + 1];
	}

	return true;
}