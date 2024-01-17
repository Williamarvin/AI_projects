## Potential include pakages in C++

```cpp
\#include <iostream>
\#include <opencv2/opencv.hpp>
\#include <opencv2/highgui/highgui.hpp>
\#include <opencv2/imgproc/imgproc.hpp>
\#include "NumCpp.hpp"
```

## Useful code support for C++

Read images and show images in C++ using OpenCV

```cpp
 // Read the image in BGR format
    cv::Mat im = cv::imread("./elephant.jpg");

    if (im.empty()) {
        std::cout << "Could not open or find the image" << std::endl;
        return -1;
    }

    // Convert the image from BGR to RGB format
    cv::cvtColor(im, im, cv::COLOR_BGR2RGB);

    // Print the shape/size of the image
    std::cout << im.rows << " x " << im.cols << " x " << im.channels() << std::endl;

    // Display the image in a window
    cv::namedWindow("Image", cv::WINDOW_AUTOSIZE);
    cv::imshow("Image", im);
    cv::waitKey(0);  // Wait for a keystroke in the window

    // Flatten each channel of the image
    cv::Mat all_pixels = im.reshape(1, im.rows * im.cols);
    std::cout << all_pixels.rows << " x " << all_pixels.cols << std::endl;
```

Read features in C++ using Numcpp

```cpp
auto label_hxyz = nc::load<long>("pred_np.bin");
label_hxyz.reshape({51529, 2048}); // Deep model based features in Problem 1 are (51529, 2048)
```

