---
title: Color Management Overview
apple_id: TP30001148
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/csintro/csintro_ovrvw/csintro_ovrvw.html
archived_at: '2026-07-15T07:38:07.615238Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Color Management Overview](Introduction%20to%20Color%20Management%20Overview.md)


[Next](Color%20Spaces.md)[Previous](Introduction%20to%20Color%20Management%20Overview.md)

# Color: A Brief Overview

Color is a sensation and, therefore, a subjective experience. The sensation of color is one component of the visual sensation, caused by the sensitivity of the human eye to light. Light can be perceived either directly from light sources (such as the sun, a fire, incandescent or fluorescent bulbs, television screens, and computer displays) or indirectly, when light from these sources is transmitted through or reflected by objects. Color sensation is also affected by how the brain processes information and is specific to each individual. Thus color perception is a very complex phenomenon.

The foundation of the color reproduction process is trichromatic color vision, which describes the capacity of the human eye to respond equally to two or more sets of stimuli having different visible spectra. This means that two or more visible spectra may exist that will be perceived as the same color, a phenomenon known as metamerism. Because of this property, spectral color reproduction, a very expensive and impractical process, can be replaced by trichromatic color reproduction, a process that is much cheaper and easier to control.

Trichromatic color reproduction induces the illusion of a color using various amounts of only three primary colors: either red, green, and blue mixed additively or cyan, magenta, and yellow mixed subtractively. Additive and subtractive colors are described in [Additive and Subtractive Color](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbyfvbuqmrqguwueq2jjfdeuqkk). Trichromatic color reproduction is the fundamental mechanism used in the majority of color reproduction devices, from television, computer display and movie screens, to magazines, newspapers, large posters, and small pages printed on your desktop printer.

Computers enable you to control color digitally and many peripherals have been developed for acquiring, displaying, and reproducing color. As a result, there is a need for a mechanism to maintain color control in an environment that can include different computer operating systems and hardware, as well as a wide variety of devices and media connected to the computer.

The eye contains two types of receptors, cones and rods. The rods measure illumination and are not sensitive to color. The cones contain a chemical known as Rhodopsin, which is variously sensitive to reds and blues and has a default sensitivity to yellow. The color the eyes see in an object depends on how much red, green, and blue light is reflected to a small region in the back of the eye called the fovea, which contains a great majority of the cones present in the eye. Black is perceived when no light is reflected to the eye.

Even the conditions in which color is viewed greatly affect the perception of color. The light source and environment must be standardized for accurate viewing. When viewing colors, people in the graphic arts industry, for example, avoid fluorescent and tungsten lighting, use a particular illuminant that is similar to daylight, and proof against a neutral gray surface.

Color images frequently contain hundreds of distinctly different colors. To reproduce such images on a color peripheral device is impractical. However, a very broad range of colors can be visually matched by a mixture of three “primary” lights. This allows colors to be reproduced on a display by a mixture of red, green, and blue lights (the primary colors of the additive color space shown in [Figure 2-4](Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbyfvbuqmrsgiwueq2jjjeegrck)) or on a printer by a mixture of cyan, magenta, and yellow inks or pigments (the primary colors of the subtractive color space shown in [Figure 2-4](Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbyfvbuqmrsgiwueq2jjjeegrck)). Black is printed to increase contrast and make up for the deficiency of the inks (making black the key, or K, in CMYK).

Color is described as having three dimensions. These dimensions are hue, saturation, and value. Hue is the name of the color, which places the color in its correct position in the spectrum. For example, if a color is described as blue, it is distinguished from yellow, red, green, or other colors. Saturation refers to the degree of intensity in a color, or a color’s strength. A neutral gray is considered to have zero saturation. A saturated red would have a color similar to apple red. Pink is an example of an unsaturated red. Value (or brightness) describes differences in the intensity of light reflected from or transmitted by a color image. The hue of an object may be blue, but the terms dark and light distinguish the value, or brightness, of one object from another. The 3-dimensional color spaces based on hue, saturation and value are described in [HSV and HLS Color Spaces](Color%20Spaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbyfvbuqmrsgiwueq2jjbbucq2c).

The additive color theory refers to the process of mixing red, green, and blue lights, which are each approximately one-third of the visible spectrum. Additive color theory explains how red, green, and blue light can be added to make white light. Red and green projected together produce yellow, red and blue produce magenta, and blue and green produce cyan. With red, blue, and green transmitted light, all the colors of the rainbow can be matched.

The subtractive color theory refers to the process of combining subtractive colorants such as inks or dyes. In this theory, various levels of cyan, magenta, and yellow absorb or “subtract” a portion of the spectrum of white light that is illuminating an object. The color of an object is the result of the color lights that are not absorbed by the object. An apple appears red because the surface of the apple absorbs the blue and green light.

Monitors use the additive color space, output printing devices use the subtractive color space.

[Next](Color%20Spaces.md)[Previous](Introduction%20to%20Color%20Management%20Overview.md)

