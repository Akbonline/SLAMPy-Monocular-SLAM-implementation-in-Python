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
<br />
<p align="center">
    _________.____       _____      _____ __________        
 /   _____/|    |     /  _  \    /     \\______   \___.__.
 \_____  \ |    |    /  /_\  \  /  \ /  \|     ___<   |  |
 /        \|    |___/    |    \/    Y    \    |    \___  |
/_______  /|_______ \____|__  /\____|__  /____|    / ____|
        \/         \/       \/         \/          \/     

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/JUOY5DrO8R8">View Demo</a>
    ·
    <a href="https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python/issues">Report Bug</a>
    ·
    <a href="https://github.com/Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
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
* [numPy](https://numpy.org/)


<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* openCV 4
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
git clone Akbonline/SLAMPy-Monocular-SLAM-implementation-in-Python.git
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


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



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

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=flat-square
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=flat-square
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
