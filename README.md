# SLAMPy-Monocular-SLAM-implementation-in-Python
Pythonic implementation of an ORB feature matching based Monocular-vision SLAM. 
<!--
*** Thanks for checking out the application. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "Added this change".
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
![logo](https://user-images.githubusercontent.com/35187768/97795512-429c1f80-1bc4-11eb-9580-8a5bf63d839a.png)

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Simultaneous Localization and Mapping (SLAM) has been there for quite a while, but it has gained much popularity with the recent advent of Autonomous Navigation and self-driving cars. SLAM is like a perception that aids a robot/device to find it's relative position in an unknown environment. Applications of which extend from Augmented Reality, virtual reality, indoor navigation and Autonomous vehicles. 

### Built With
This section should list any major frameworks that you built your project using. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.
* [Python3](https://www.python.org/download/releases/3.0/)
* [PyGame](https://www.pygame.org/)
* [G2OPy](https://github.com/uoip/g2opy)
* [Pangolin](https://github.com/uoip/pangolin)
* [OpenCV](https://pypi.org/project/opencv-python/)
* [NumPy](https://numpy.org/)


<!-- GETTING STARTED -->
## Getting Started
The application begins with calibrating the camera and setting the camera intrinsic for optimization. It makes use of OpenCV's ORB feature mapping function for key-point extraction. Lowe's ratio test is used for mapping the key-points. Each detected key-point from the image at '(t-1)' interval is matched with a number of key-points from the 't' interval image. The key-points with the least distance is kept based on the several generated. Lowe's test checks that the two distances are sufficiently different. If they are not, then the key-point is eliminated and will not be used for further calculations. For 2D video visualization, I had a couple of choices: OpenCV, SDL2, PyGame, Kivy, Matplotlib, etc. Turns out OpenCV's imshow function might not be the best choice. The application made use of SDL2, matplolib and kivy's video playing libraries but PyGame was outperformed all of them. Thus, I used PyGame for visualizing the detected keypoints and various other information such as orientation, direction and speed.

![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/35187768/97795406-159b3d00-1bc3-11eb-9a7e-2f8caef2bac9.gif)


For 3D visualization, Pangolin was the best option due to various reasons such as:

* Supports python and it's opensource!
* Uses simple OpenGL at its fundamental form
* Provides Modularized 3D visualization
For implementing a graph-based non-linear error function, the project leverages the python wrapper of G2O library. G2O is an open-source optimization library that helps reduce the Gaussian Noise from nonlinear least squares problems such as SLAM.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* OpenCV 4
```sh
pip3 install opencv-python
```
* PyGame
```sh
python3 -m pip install -U pygame --user
```
* NumPy
```sh
pip3 install numpy
```
* g2oPy
  * [Please see here](https://github.com/uoip/g2opy)
* Pangolin
  * [Please see here](https://github.com/uoip/pangolin)

### Installation

1. Clone the repository:
```sh
git clone https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python.git
```
2. Running the algorithm on a video
```sh
python3 slam.py <test-video.mp4>
```

<!-- USAGE EXAMPLES -->
## Usage

There is one test video included in the repo.

1. To run the test video
```sh
python3 slam.py test.mp4
```
The output should look something like this:

![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/35187768/97795404-1207b600-1bc3-11eb-95e7-5dbcd1419310.gif)

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

* Akshat Bajpai - [My Portfolio](https://www.akbexpo.com) 
* Email: akshatbajpai.biz@gmail.com
* Project Link: [https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python](https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python)
* My LinkedIn: [linkedin-url]: (linkedin.com/in/akshat-bajpai)
* My GitHub: [linkedin-url]: (https://github.com/Akbonline)
<iframe width="560" height="315" src="https://www.youtube.com/embed/JUOY5DrO8R8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [g2oPy](https://github.com/uoip/g2opy)
* [Pangolin](https://github.com/uoip/pangolin)
* [GeoHotz](https://github.com/geohot)
* [GSLAM](https://github.com/zdzhaoyong/GSLAM)

[contributors-shield]: https://img.shields.io/github/contributors/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python.svg?style=flat-square
[contributors-url]: https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python.svg?style=flat-square
[forks-url]: https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python/network/members
[stars-shield]: https://img.shields.io/github/stars/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python.svg?style=flat-square
[stars-url]: https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python/stargazers
[issues-shield]: https://img.shields.io/github/issues/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python.svg?style=flat-square
[issues-url]: https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python/issues
[license-shield]: https://img.shields.io/github/license/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python.svg?style=flat-square
[license-url]: https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/akshat-bajpai
[product-screenshot]: https://user-images.githubusercontent.com/35187768/97795404-1207b600-1bc3-11eb-95e7-5dbcd1419310.gif
