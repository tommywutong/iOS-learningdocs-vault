---
title: Color Spaces – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/color-spaces/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:39c23cc8e3fdf4bd'
translated: false
---

> 原文：[Color Spaces – Bartosz Ciechanowski](https://ciechanow.ski/color-spaces/)　·　Bartosz Ciechanowski

# [Color Spaces](https://ciechanow.ski/color-spaces/)

For the longest time we didn’t have to pay a lot of attention to the way we talk about color. The modern display technologies capable of showing more vivid shades have, for better or for worse, changed the rules of the game. Once esoteric ideas like a gamut or a color space are becoming increasingly important.

A color can be described in many different ways. We could use words, list amounts of [CMYK](https://en.wikipedia.org/wiki/CMYK_color_model) printer inks, enumerate [quite flawed](https://en.wikipedia.org/wiki/HSL_and_HSV#Disadvantages) HSL and HSV values, or even quantify [the responses of cells](https://en.wikipedia.org/wiki/LMS_color_space) in a human retina. Those notions are useful in some contexts, but I’m not going to focus on any of them.

This article is dedicated entirely to RGB values from RGB color spaces. It may seem fairly restrictive, but considering the domination of displays as the medium for color presentation, it is a pragmatic approach and it ultimately won’t prevent us from describing everything we can see.

A dry definition of a color space is not a good way to kick things off. Instead, we’ll start by playing with one of the most common tools used to specify colors.

# Color Pickers[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#color-pickers)

You’ve probably seen an RGB color picker before, it usually looks like this:

By dragging all the sliders to the right you can create a [white](#) color. Lots of red and green with little blue produces shades of [yellow](#). That color picker is not the only way to specify colors. Try using the one below:

The gist of the behavior of that new picker is the same – the red slider controls the red component, the green slider affects the green component, and the blue slider acts on the blue component. Both sets of sliders have the minimum value of 0 and the maximum value of 255. However, the shades and intensities they create are quite different. We can compare some of the colors for the same slider positions side by side. In each plate the top half shows the color from the first picker and the bottom half contains the color from the second picker:

The only color that looks the same is a pure black, none of the other colors match despite the same values of red, green, and blue. You may be wondering which halves of the plates are wrong, but the truth is that they’re both correct, they just come from different RGB color spaces.

I’ll soon explain what causes those differences and we’ll eventually see what defines a color space, but for now the important lesson is that on their own the numeric values of the red, green, and blue components have _no meaning_. A color space is what assigns the meaning to those numeric values.

What I’ve shown you above is an extreme example in which almost everything about the two color spaces is different. Over the course of the next few paragraphs we will be looking at simpler examples which will help us get a feel for what different aspects of color spaces mean. Before we discuss those aspects we should make a quick detour to revisit how the components of an RGB color are described.

# Normalized Range[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#normalized-range)

When dealing with RGB colors you’ll often see them specified in a 0 to 255 range:

255, 230, 26

Or in an equivalent hexadecimal form:

ff, e6, 1a

While using the range of 0 to 255 is convenient, especially for specifying colors on the web, it ties the description of color to a specific 8-bit depth. What we actually want to express is the _percentage_ of the maximum intensity a red, green, or blue component can represent.

In our discourse I’ll use a so called _normalized_ range where the minimum value is still 0.0, but the maximum value is 1.0. Calculating normalized values from 0 to 255 range is easy – just divide the source numbers by 255.0:

1.000, 0.902, 0.102

This form may feel less familiar, but it lets us talk about the values without having to care what kind of discrete encoding scheme they’ll eventually use.

# Intensity Mismatch[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#intensity-mismatch)

Let’s continue playing with the color pickers by upgrading them to show two colors at the same time. In the top half we’ll see the color obtained from the RGB values interpreted by one color space, while the bottom half shows the color obtained from _the same_ RGB values, but interpreted by another color space:

While playing with the sliders you may have noticed something peculiar – if the sliders are at their minimum or maximum the colors look the same, otherwise they don’t. Here’s a comparison of some of the colors for different slider values:

A color space can specify how the numeric values of the red, green, and blue components map to intensity of the corresponding light source. In other words, the position of a slider may not be equal to intensity of the light the slider controls. The color space from the bottom half uses a simple linear encoding:

(intensity value) = (encoded value)

The light shining at 64% of its maximum intensity will be encoded as the number 0.64. The top color space uses an encoding with a fixed 2.0 exponent:

(intensity value) = (encoded value)^2.0

The light shining at 64% of its maximum intensity will be encoded as 0.8.

This may seem all like a pointless transformation, but there is a good reason for doing all this nonlinear mapping. The human eye is not a simple detector of the power of the incoming light – its response is nonlinear. A two-fold increase in emitted number of photons per second will _not_ be perceived as twice as bright light.

If we were to encode the colors using [floating point numbers](https://ciechanow.ski/exposing-floating-point/) the need for a nonlinear encoding function would be diminished. However, the numeric values of color are often encoded using the familiar 8 bits per component, e.g. in the most common configurations of [JPEG](https://en.wikipedia.org/wiki/JPEG) and [PNG](https://en.wikipedia.org/wiki/Portable_Network_Graphics) files. Using a nonlinear _tone response curve_, or TRC for short, lets us maintain more or less _perceptual_ uniformity and use the chunky, quantized range to keep the detail in the darker parts.

Here are the first 14 representable values in 8 bit encoding of linearly increasing amount of light. You can probably tell that the brightness difference we perceive between the first two panes is much larger than between the last two panes:

![First 14 representable linear shades of gray in 8 bit encoding](https://ciechanow.ski/images/color_8_bit_linear.svg)

First 14 representable linear shades of gray in 8 bit encoding

The extremely common [sRGB](https://en.wikipedia.org/wiki/SRGB) color space employs a nonlinear TRC to make a better use of the human visual perception. Here are the first 14 representable values in an 8 bit encoding of output sRGB values. You may need to ramp up your display brightness to see them, or maybe even [make the background black](#)[make the background bright](#):

![First 14 representable sRGB shades of gray in an 8 bit encoding](https://ciechanow.ski/images/color_8_bit_srgb.svg)

First 14 representable sRGB shades of gray in an 8 bit encoding

Notice the hollow circles under all but the first and the last colors. None of those 12 shades of gray would be representable in an 8 bit format if we were to use straightforward linear encoding. You’d actually need a range of 0 to 4095 (12 bits per component) to represent the same very dark shades of sRGB gray without using any tone response curves.

The situation at the other end of the spectrum is more difficult to visualize since the images on this website use sRGB color space, but we can at least show that the white shades in linear color space shown in the upper part of the picture get darker more slowly than corresponding white shades in sRGB at the bottom:

![Last 14 representable linear (top) and sRGB (bottom) shades of gray in an 8 bit encoding](https://ciechanow.ski/images/color_8_bit_white.svg)

Last 14 representable linear (top) and sRGB (bottom) shades of gray in an 8 bit encoding

Linear encoding has the same precision of light intensity everywhere, which accounting for our nonlinear perception ends up having very quickly increasing brightness at the dark end and very slowly decreasing darkness at the bright end.

Different color spaces use different TRCs. Some, like [DCI P3](https://en.wikipedia.org/wiki/DCI-P3), use a simple power function with a fixed exponent. Others, like [ProPhoto](https://en.wikipedia.org/wiki/ProPhoto_RGB_color_space) employ a piecewise combination of a linear segment with a power segment. The magnitude of the exponent differs between color spaces – there is no unanimous opinion on what constitutes the best encoding. Finally, some color spaces don’t use any special encoding and just represent the component values in linear fashion.

While TRCs are very useful for _encoding_ the intensities for storage, the crucial thing to remember is that mathematical operations on light only make sense when done on _linear_ values, because they represent the actual intensities of light. It’s actually fairly easy to visualize in a gradual mix between a pure red and a pure green:

Notice how in the top halves, which use nonlinear encoding, the colors get darker in the middle, while in the bottom, linear halves the progression looks more balanced.

What we’ve discussed in this section is the first component of a typical RGB display color space. We can now say that one of the defining properties of a color space is:

A set of tone response curves for its red, green, and blue components.

The encoding is an essential, but nonetheless, technical part of a color space. The specification of the actual colors is what we usually care about the most.

# Primary Differences[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#primary-differences)

Let’s look at a different example of two color spaces in a color picker. To make things simpler, both halves operate with linear intensities:

Notice that grayscale colors now match perfectly, however, the colors in the bottom half are clearly more subdued for the same numeric value:

I’ll symbolize the red, green, and blue values from the top half with a small bar on top of the letters: RGB. For the values from the bottom half I’ll use a bar at the bottom: RGB.

You may be wondering if, despite a rather different behavior, it is possible to make the colors match. In other words, knowing the RGB values we’d like to express the same color using RGB values.

The notion may seem contrived, but the underlying ideas are important for understanding how the same color can be described by many different triplets of values. To see the scenario in action we can fix the bottom half of the picker and let the sliders control only the top color:

After some trial and error you may get pretty close, or perhaps even achieve [the exact match](#). Unless you’re quite skilled, the task probably wasn’t trivial and trying to do the same manual work for every possible color would be a daunting endeavor.

A consistent reproduction of color is crucial for realizing any design – we wouldn’t want a carefully selected shade of pastel beige to look like a ripe orange when seen on some other device. We’re in a dire need of a better approach for trying to make the colors look the same despite a different meaning of the values of the RGB components.

# Primaries Matched[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#primaries-matched)

Reproducing arbitrary colors between different color spaces is difficult, but we can try to simplify things a little by just trying to match the pure red, green, and blue colors and seeing where it gets us. Let’s start by matching the red from the bottom plate:

Making the border between the two halves disappear may take some tweaking, but eventually we can agree on values [that fit perfectly](#). It’s a step in the right direction – since we’re dealing with linear values we can now express how much a single unit of R will contribute to RGB components. For instance, to recreate the RGB color of 0.60.00.0 we’d need to use:

0.6 × 0.712 = 0.427 units of R  
 0.6 × 0.100 = 0.060 units of G  
 0.6 × 0.024 = 0.014 units of B

We can put these results into equations. When a color from the RGB space has no green and no blue, but some amount of red, we could use the following formulas to see the same color in the top plate:

R = 0.712×R  
 G = 0.100×R  
 B = 0.024×R

We can repeat the experiment for pure G:

Having decided on the [the perfect match](#), we can write down the impact of G on RGB components:

R = 0.221×G  
 G = 0.690×G  
 B = 0.000×G

All that’s left is to repeat the experiments for pure B. If you’re still not tired of dragging the sliders you can do it yourself, or just [let me do it](#):

Once again, the results can be written down as:

R = 0.067×B  
 G = 0.210×B  
 B = 0.976×B

The provided equations apply only when the RGB half shows just some amount of red, _or_ just some amount of green, _or_ just some amount of blue. Being limited to having non-zero values in only one component won’t get us far. To create a more diverse set of colors we need to have a way of finding out how _mixes_ of basic components in RGB affect values in RGB.

# Mixing Things Up[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#mixing-things-up)

Thankfully, [Grassmann’s laws](https://en.wikipedia.org/wiki/Grassmann%27s_laws_(color_science)) come to our rescue. Those empirical rules tell us that if two colored lights match, then after addition of another set of matching light sources their overlap, or their sum, will also match:

![The sum of two matching sets of colored lights also matches](https://ciechanow.ski/images/color_grassman@2x.png)

The sum of two matching sets of colored lights also matches

As a result we can do the three matchings for R, G, and B separately, then just combine the results into one set. For instance, to obtain the final R value from RGB all we need to do is to sum the contribution of R to R, the contribution of G to R, and the contribution of B to R. Repeating the trick for the other two components yields the following set of equations:

R = 0.712×R + 0.221×G + 0.067×B  
 G = 0.100×R + 0.690×G + 0.210×B  
 B = 0.024×R + 0.000×G + 0.976×B

What we just did was a matching of [primary](https://en.wikipedia.org/wiki/Primary_color) red, green, and blue colors from one color space to another. With the equations in hand we can finally recreate the math behind the matching beige from the first example. By plugging in the original RGB values of 0.90.50.2 we can calculate the value of the exact match:

R = 0.712×0.9 + 0.221×0.5 + 0.067×0.2 = 0.765  
 G = 0.100×0.9 + 0.690×0.5 + 0.210×0.2 = 0.477  
 B = 0.024×0.9 + 0.000×0.5 + 0.976×0.2 = 0.217

# Seeing the Matrix[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#seeing-the-matrix)

If you look closely at the three equations governing the conversion from RGB to RGB you may notice the coefficients form a 3×3 grid:

0.7120.2210.067  
 0.1000.6900.210  
 0.0240.0000.976

It’s actually a 3×3 matrix that defines the conversion from RGB to RGB. If you’re familiar with matrices and vectors, you might have already realized that the transformation we did was a plain old matrix times vector multiplication.

On its own the matrix isn’t particularly interesting, but the transformation it does can be visualized in 3D. In the following interactive diagram the outer cube defines the RGB space, while the inner, skewed cube ([parallelepiped](https://en.wikipedia.org/wiki/Parallelepiped)) defines the RGB space. You can drag the cubes around to see them from different angles and control the RGB color indicator using the sliders:

As an experiment I encourage you to [set](#) red and green components to 0 and just play with the blue slider. You should be able to see that movement along the pure blue color in RGB space requires some shift in red and green in RGB.

Notice that RGB parallelepiped fits completely inside RGB cube which means that one can recreate every single RGB color using RGB space. The inverse, however, is not true.

# There and Back Again[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#there-and-back-again)

In the example below the background of the top half is set to a pure R at maximum intensity. You may try really hard, but there is no combination of values in RGB that can cause the seam between the two halves to disappear:

If we ignore the issue for a minute and treat the problem algebraically we can solve the system of 3 equations looking for pure R at the output:

1.0 = 0.712×R + 0.221×G + 0.067×B  
 0.0 = 0.100×R + 0.690×G + 0.210×B  
 0.0 = 0.024×R + 0.000×G + 0.976×B

The details of the evaluation are boring, so let’s just present the solution as is:

R = +1.470  
 G = −0.201  
 B = −0.036

All three values are outside of 0.0 to 1.0 range – a clear indication of the unreachability of that color in RGB space!

Values larger than 1.0 have a very straightforward explanation: 1.0 of R is beyond the range of intensity of R, you could say that R is not strong enough. Some less intense values of R _can_ contribute to R within limit. For example, 0.5 of R requires 0.5 × 1.470 = 0.735 of R.

Negative values are slightly trickier because they are imaginary, but we can still reason about them quite easily.

# Negative Values[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#negative-values)

Let’s try to think about an experiment in which we’re tasked with matching a light on the right side with a combination of a red, green, and blue light on the left side:

![Mixing lights to obtain the color on the right](https://ciechanow.ski/images/color_negative_0@2x.png)

Mixing lights to obtain the color on the right

After some tuning we may realize that even with no green and no blue light the colors still don’t match and the left patch of light continues to look a bit orangey indicating that it has too much green in it:

![The left patch is still too green](https://ciechanow.ski/images/color_negative_1@2x.png)

The left patch is still too green

We can’t decrease the green light on the left side anymore, so we have to become more creative. We could say that the left side is too green, _or_ we could say that the right side is not green enough! Since all we care about is making the colors match we could try adding some of the green light to the _other_ side:

![Adding green light to the target side](https://ciechanow.ski/images/color_negative_2@2x.png)

Adding green light to the target side

Now the right side is too green, but if we adjust the added amount we can eventually make the colors look the same:

![A match with just the right amount of green](https://ciechanow.ski/images/color_negative_3@2x.png)

A match with just the right amount of green

Let’s try to write down what we’ve achieved in an equation. We have a maximum amount of red and no green or blue on the left side, while on the right side we have the target color with some green light added to it:

1.0×R + 0.0×G + 0.0×B = (target) + 0.2×G

This feels a little mischievous – we wanted to match the pure target color without any additions. Let’s try to rearrange the equation by moving the added green light from the right to the left side:

1.0×R − 0.2×G + 0.0×B = (target)

That equivalent equation tells us that getting the exact match with the starting target color requires using a _negative_ amount of the green light on the left side. Naturally, this is something we can’t do in a physical world. Mathematically, however, a match of the very saturated red from the right side really requires removing some green light from the left side.

If you’re still not convinced consider what would happen if we somehow were able to create −0.2×G on the left side. I can’t show you a picture of that imaginary situation, but I can show you what would happen if we then added 0.2×G to _both_ sides:

![](https://ciechanow.ski/images/color_negative_3@2x.png)

This is exactly the same image as before since both scenarios are equivalent. Recall from Grassmann’s laws that adding the same amount of light to both sides maintains the color match, so indeed the imaginary −0.2×G on the left side must have made it look like the original unmodified saturated red from the right side.

This may all be somehow unsatisfying, however, when you step away from the physical restrictions and think about lights as just numbers, it all, quite literally, adds up.

# The Matrix Seeing[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#the-matrix-seeing)

If we go back to our quest for obtaining RGB values from RGB colors we can repeat the “system of equations” trick for the other two components and combine the results using Grassmann’s laws to end up with the full set of equations:

R = +1.470×R − 0.470×G + 0.000×B  
 G = −0.201×R + 1.513×G − 0.311×B  
 B = −0.036×R + 0.011×G + 1.025×B

Once again, the set of coefficients can be presented in a 3×3 matrix:

+1.470−0.470+0.000  
 −0.201+1.513−0.311  
 −0.036+0.011+1.025

If you’ve solved systems of linear equations before, you may have realized that this is just an [inverse matrix](https://www.wolframalpha.com/input/?i=inverse+%5B%5B0.712,0.221,0.067%5D,%5B0.100,0.690,0.210%5D,%5B0.024,0.000,0.976%5D%5D) of the original RGB to RGB transformation. This is a very useful property. When establishing the conversion from one linear color space to another we just need to figure out the coefficients of the matrix in one direction – the matrix in the other direction is just its inverse.

One more time we can visualize the transformation the matrix performs. This time RGB is the perfect cube, while RGB is the outer skewed cube:

You can easily see how much bigger the RGB space is and indeed it lets us express some colors that RGB can’t.

# Breaking the Boundaries[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#breaking-the-boundaries)

So far whenever a numeric value in a color space was outside of 0.0 to 1.0 range we’d just clip it to the representable limits. Let’s try to see what happens when we remove that restriction. We can modify the sliders to allow −1.0 to 2.0 range and try to match the pure R again:

With that approach we can actually [represent](#) the pure R using RGB color space. Since the numbers don’t care, the entire thing works and is often called _unbounded_ or _extended_ range.

To actually see RGB colors represented using extended range RGB colors the display has to be capable of showing RGB colors in the first place, otherwise they would get physically clamped by the display itself. To put it differently, the transformation of values from a color space with extended range to the native color space of the display should end up with the values in a standard range.

While unbounded values are very flexible, there are two important caveats one should consider when dealing with them. First of all, since the range of values is unlimited, it is possible to create colors that truly have no physical meaning, e.g. −1.0−1.0−1.0.

Additionally, storing the values in a type with a limited range may not be possible. If we decide to use 8 bits per component and encode the 0.0 to 1.0 range into 0 to 255 range then we won’t be able to represent the values outside of normalized range since they simply won’t fit.

# One Space to Rule Them All[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#one-space-to-rule-them-all)

All the color transformations we performed are somewhat contrived – the two color spaces we analyzed are defined in relation to each other and have no immutable attachment to the physical world. Their reds, greens, and blues are whatever we ended up seeing on the screen. We have no way of knowing how the colors would look on another device.

If we had a master color space that was derived from physical quantities we could solve the problem by finding a transformation from any color space to that common connection space. Luckily, in 1931 that very color space has been specified by [CIE](https://en.wikipedia.org/wiki/International_Commission_on_Illumination) and resulted in what is known as [CIE 1931 XYZ color space](https://en.wikipedia.org/wiki/CIE_1931_color_space). Before we discuss how the space was defined we need to take a quick look at physics and the human visual system.

# And There Was Light[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#and-there-was-light)

To ground the discussion of color perception in the real world we have to establish it in terms of light – the part of [electromagnetic radiation](https://en.wikipedia.org/wiki/Electromagnetic_radiation) that is visible to the human eye. The [visible spectrum](https://en.wikipedia.org/wiki/Visible_spectrum) can only be approximated on a typical display, but its colors at specific wavelengths look roughly like this:

![Visible spectrum with wavelengths shown in nanometers](https://ciechanow.ski/images/color_spectrum.svg)

Visible spectrum with wavelengths shown in nanometers

Colors corresponding to a single wavelength are called [spectral colors](https://en.wikipedia.org/wiki/Spectral_color). For example, a light with wavelength of 570 nm would produce a pure spectral yellow. Notice that boundaries between the colors are soft, so there is no single “spectral red”, but a wavelength is all we need to describe a spectral color accurately.

Human eyes are not simple wavelength detectors and the perception of the same color can be created in many different ways. A yellow color can be created using light with wavelength around 570 nm, _or_ as a mixture of a green and a red light.

Since a human retina has three different types of photoreceptive [cones](https://en.wikipedia.org/wiki/Cone_cell), any color sensation can be matched using three fixed colors with varying intensities. It doesn’t mean that _all_ colors can be recreated using just additive mixes of three colors. As we’ve discussed, sometimes one or two of those colors have negative weights and have to be added to the target color instead.

Algebraically, however, we don’t need more than three primary colors to represent everything humans can perceive (with some very rare [exceptions](https://theneurosphere.com/2015/12/17/the-mystery-of-tetrachromacy-if-12-of-women-have-four-cone-types-in-their-eyes-why-do-so-few-of-them-actually-see-more-colours/)). This property of the human visual system is called [trichromacy](https://en.wikipedia.org/wiki/Trichromacy) and is exploited by various display technologies to present a very broad spectrum of colors using just three RGB primaries.

# The Color Matching Experiments[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#the-color-matching-experiments)

At the beginning of the 20^th century David Wright and John Guild independently conducted experiments with human observers in which the test subjects tried to match the spectral colors in 10 nm increments with a combination of red, green, and blue light sources. The experiments were fairly similar to what’ve been doing with the sliders trying to match the target color as a combination of some other three colors.

The results of the experiments were standardized as rgb color matching functions that can be presented on a graph:

![CIE rgb color matching functions](https://ciechanow.ski/images/color_matching.svg)

CIE rgb color matching functions

Notice the presence of negative values. Not all spectral colors could be achieved by a combination of selected RGB values and yet again a negative value means that the color was added to the target value.

The CIE standardized the reference R of the experiments as monochromatic light with wavelength of 700.0 nm, the reference G as 546.1 nm, and the reference B as 435.8 nm, with specific ratio of relative intensities between them. This is a critical step in our discussion of color – we’re finally grounded to some physically measurable properties.

Let’s look at the yellow wavelength of 570 nm. Reading from the color matching plot we can tell that the color match required 0.16768 units of R, 0.17087 units of G and −0.00135 units of B. A set of three RGB coordinates just begs for a three dimensional presentation. If we read the color matching value for every wavelength we obtain the following plot:

You may wonder why the spectrum curve doesn’t go through the pure red, green, or blue endpoints of the CIE RGB cube, but it’s simply the result of normalization and scaling applied to the color matching functions by the committee. Within reasonable limits a light source can be constructed to be as powerful as needed, so what constitutes a “1.0” is always defined somehow arbitrarily.

# XYZ Space[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#xyz-space)

CIE RGB color space is rooted to concrete physical properties of monochromatic lights and we could use it to define any color sensation. However, the committee strived to create a derived space that would have a few [useful properties](https://en.wikipedia.org/wiki/CIE_1931_color_space#Construction_of_the_CIE_XYZ_color_space_from_the_Wright%E2%80%93Guild_data), two of which are worth noting:

- No negative coordinates of spectral colors
- Separation of [chromaticity](https://en.wikipedia.org/wiki/Chromaticity) (hue and colorfulness) from [luminance](https://en.wikipedia.org/wiki/Luminance) (visual perception of brightness)

After some deliberation the following set of equations was created:

X = 2.769×R + 1.752×G + 1.130×B  
 Y = 1.000×R + 4.591×G + 0.061×B  
 Z = 0.000×R + 0.057×G + 5.594×B

The factors may seem arbitrary, and in some sense they are, but this is simply yet another mapping of values from one space to another, similar to what we did with RGB to RGB transformation. The Y component was chosen as the luminance component, while X and Z define the chromaticity.

We can visualize the CIE XYZ space inside the CIE RGB space:

You can see how the XYZ space is designed around the spectrum curve to make sure it fits in the positive octant. Its smaller size is not really a concern, the scaling makes things more convenient to work with by making sure the perceptually brightest wavelength of 555 nm has a Y value of 1. As a final step we can just show the XYZ space and the spectral colors on their own:

Since the CIE XYZ space is derived from CIE RGB it is also grounded in measurable physical quantities. The XYZ color space is the base color space used for all conversions of matrix-based RGB display color spaces. The mapping between any two color spaces is done through a common CIE XYZ intermediate. This simplifies the color transformations since we don’t need to know how to convert colors between any two arbitrary color spaces, we just need to be able to convert both of them to the XYZ space.

# xy Chromaticity Diagram[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#xy-chromaticity-diagram)

Three dimensional diagrams are fun to play with, but they’re often not particularly practical – a 2D plot is often easier to work with and reason about. Since the Y component of the XYZ space is devoid of any colorfulness and hue, we’re left with only two components that affect the chromaticity of a color. We can perform three operations intended to reduce the dimensionality of the space:

x = X / (X + Y + Z)  
 y = Y / (X + Y + Z)  
 z = Z / (X + Y + Z)

The distinction between a lower and an upper case is important here – X is not the same as x. These seemingly arbitrary equations have a simple visual explanation – it’s a projection onto a triangle spanned between XYZ coordinates of 1.00.00.0, 0.01.00.0, and 0.00.01.0:

Notice that x, y, and z add up to 1, so we can drop the last component since it’s redundant – we can always recreate it by subtracting x and y from 1. Rejection of z is equivalent to a flat projection onto xy plane:

If we repeat that step for _every_ combination of spectral colors we can finally present the 2D plot known as CIE xy chromaticity diagram in its full glory. You may have seen this horseshoe shape before:

![CIE xy chromaticity diagram](https://ciechanow.ski/images/color_chroma.svg)

CIE xy chromaticity diagram

No RGB display technology is capable of presenting all the colors that humans can see, so many of the ones shown in the picture are actually the result of clamping to the representable range of the sRGB color space.

The colors on the inside of the plot are just some combinations of the spectral colors and the colors outside of the plot [don’t exist](https://en.wikipedia.org/wiki/Impossible_color#Imaginary_colors). Notice the straight diagonal line connecting the end points of the red and blue area. While every point on the outline of the horseshoe shape has a corresponding spectral wavelength, the colors on that [line of purples](https://en.wikipedia.org/wiki/Line_of_purples) do not – there is no wavelength of light that looks like magenta. The purples are simply how the human brain interprets the mixes of red and blue light and ultimately they are no different than any other shade. Perception of _every_ color happens in our heads.

It’s important to mention that the xy chromaticity diagram is not perceptually uniform. In some areas of the plot one has to move relatively far away from a chosen color to notice the difference in chromaticity, while in some other areas the distance to change is [much smaller](https://en.wikipedia.org/wiki/MacAdam_ellipse). Over time CIE developed more uniform [chromaticity diagrams](https://en.wikipedia.org/wiki/CIELUV#/media/File:CIE_1976_UCS.png), but since the xy diagram is easily obtained from the XYZ space it continues to be used in discussion of RGB color spaces.

# Gamut[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#gamut)

The chromaticity diagram is useful in visualizing the [gamut](https://en.wikipedia.org/wiki/Gamut) of a color space – the extent of colors that a color space can represent. It’s necessary to note that a gamut is a three dimensional construct, so a 2D projection onto an image, somehow contrarily, does _not_ present a full picture. It’s nonetheless a useful tool employed in comparison of color spaces.

We can finally present the chromaticities of primaries of both RGB and RGB color spaces in a single graph:

![Comparison of primaries](https://ciechanow.ski/images/color_gamuts.svg)

Comparison of primaries

I’ll discuss the meaning of the little cross in the middle soon, but the important fact is that a triangle depicts all representable chromaticities of a color space. Notice how RGB triangle is smaller than RGB triangle showing us yet again that the latter can represent more colors.

This diagram summarizes a long journey we took to define the second component that defines every RGB color space:

Location of its red, green, and blue primaries on CIE xy chromaticity diagram.

In the simulation below you can drag the slider to see how the extent of the chromaticity triangle corresponds to the representable colors. The base values of an image from sRGB color space are converted to a space with a reduced gamut, clamped to 0.0 to 1.0 range, then finally converted back to sRGB for display. You can clicktap the image to change it:

Your browser doesn't support WebGL which is required for this demo.

In some cases the color clamping is pretty severe, but for the image with snowy mountains the change is minimal. An almost black and white picture has little chromaticity and therefore a reduced gamut has almost no effect on it.

# White Point[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#white-point)

The last aspect of color spaces we will discuss is related to the little cross in the middle of RGB and RGB gamut visualization. Similarly to how different color spaces can assign different colors to their pure red defined as 1.00.00.0, the [white point](https://en.wikipedia.org/wiki/White_point) of a color space defines its color of white – the represented color when all three components are ones 1.01.01.0.

In the color picker below both halves have the same RGB primaries, but different white points. See what happens when you [drag all the sliders to the right](#):

The color space from the bottom half defines its white as a slightly different color than the top color space.

A 3D visualization shows two interesting properties. Firstly, the axes of the inner and the outer cubes are collinear, they’re just scaled differently. Secondly, the “far” endpoints of the cubes no longer overlap since their whitepoints are different:

The white point is the last piece of the color space puzzle. We can now say that a color space is also defined by:

A location of its white point on CIE xy chromaticity diagram.

With xy coordinates of the red, green, and blue primaries, _and_ the xy coordinates of the white point one can evaluate the RGB to XYZ transformation for a given color space. The details of this computation are not critical to our discussion and you can read about them in many places online, e.g. on [Bruce Lindbloom’s website](http://www.brucelindbloom.com/index.html?Eqn_RGB_XYZ_Matrix.html).

While necessary for correct calculation of RGB to XYZ transformation, in practice it may be difficult to notice that two color spaces have different whitepoints. Most color conversion operations will undergo [chromatic adaptation](https://en.wikipedia.org/wiki/Chromatic_adaptation) and the color of 1.01.01.0 in the source color space will be mapped to 1.01.01.0 in the destination color space.

# sRGB Color Space[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#srgb-color-space)

We’ll finish our discussion with a showcase of the sRGB color space, [described by its authors](https://www.w3.org/Graphics/Color/sRGB.html) as “A Standard Default Color Space for the Internet”. If you ever were specifying just “RGB” colors it’s extremely likely that the components were assumed to come from the sRGB color space. In fact, it’s the color space used in the very [first color picker](#color-pickers) in this article.

While the sRGB [specification](https://webstore.iec.ch/publication/6169) isn’t free, [Wikipedia](https://en.wikipedia.org/wiki/SRGB) and [International Color Consortium](http://www.color.org/chardata/rgb/srgb.xalter) provide all the information we need to describe it.

## Tone Response Curve[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#tone-response-curve)

Let’s look at the plot of the tone response curve of the sRGB color space. The light intensity value is on the vertical axis and it’s symbolized with a sun icon. The encoded value is on the horizontal axis and it’s symbolized with a binary code:

![Tone response curve of sRGB](https://ciechanow.ski/images/color_srgb_trc.svg)

Tone response curve of sRGB

While the curve may look like a single power function, in the range of 0 to 0.04045 it actually is a linear segment:

(intensity value) = (encoded value)/12.92

When encoded value is larger than 0.04045 the intensity value is indeed defined by a slightly nudged power function with exponent of 2.4:

(intensity value) = (((encoded value) + 0.055)/1.055)^2.4

The transition between the two parts is continuous and I marked its location on the plot with a little bump.

The curve was designed to roughly correspond to the response curve of CRT displays thus to some extent minimizing the need for any color management. That convenience had the unfortunate consequence of creating a widespread confusion by binding the two separate ideas into one.

In general case the purpose of tone response curves is to make the best use of available space when storing the color information in formats with limited bit depth. The non-linear response of an electron gun in a CRT display is a separate and only loosely related concept.

## Chromaticity and White Point Coordinates[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#chromaticity-and-white-point-coordinates)

Chromaticity coordinates of red, green, blue, and white are just 4 pairs of x and y values and we can put them in a table:

|  | Red | Green | Blue | White |
|---|---|---|---|---|
| **x** | 0.6400 | 0.3000 | 0.1500 | 0.3127 |
| **y** | 0.3300 | 0.6000 | 0.0600 | 0.3290 |

You’ll probably agree that this form is not particularly exciting, things look much nicer on the xy chromaticity diagram:

![Chromaticity and white point coordinates of sRGB](https://ciechanow.ski/images/color_gamut_srgb.svg)

Chromaticity and white point coordinates of sRGB

On a technical note it’s worth mentioning that the primaries share the same location as [Rec. 709](https://en.wikipedia.org/wiki/Rec._709) – the standard for HDTV. Additionally, the white point location corresponds to [Standard Illuminant D65](https://en.wikipedia.org/wiki/Illuminant_D65) – a representation of the average daylight.

While sRGB isn’t capable of representing some of the more vivid shades and clearly doesn’t contain all the colors humans can see, it has served its purpose as a standard color space of 8-bit graphics remarkably well.

# Further Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#further-reading)

The web is filled with interesting gems related to color. For a very good dissection of many of the major components on a pathway between hex colors and what we end up perceiving with our eyes I suggest reading Jamie Wong’s [“Color: From Hexcodes to Eyeballs”](http://jamie-wong.com/post/color/). I especially like his very approachable explanation of spectral distributions.

Bruce MacEvoy’s [set of pages](https://www.handprint.com/LS/CVS/color.html) on color vision is an amazing resource about various aspects of color. I highly recommend the [first post](https://www.handprint.com/HP/WCL/color1.html) in the series in which the author describes the fascinating details of biophysics of the human visual system.

Elle Stone authored an extensive [collection of great articles](https://ninedegreesbelow.com/photography/articles.html) on color spaces, calibration, and image editing. For a different take on what we’ve touched upon in this article you should see [“Completely Painless Programmer’s Guide to XYZ, RGB, ICC, xyY, and TRCs”](https://ninedegreesbelow.com/photography/xyz-rgb.html).

If you think you’d enjoy a deep dive into the optimization process of creating a minimal sRGB ICC profile, Clinton Ingram has got you covered in his [four part series](https://photosauce.net/blog/post/making-a-minimal-srgb-icc-profile-part-1-trim-the-fat-abuse-the-spec). His pragmatic approach to the problem provides a very entertaining read.

Finally, as a resource in a more traditional form, I recommend the book [“Color Imaging: Fundamentals and Applications”](https://www.amazon.com/Color-Imaging-Fundamentals-Erik-Reinhard/dp/1568813449). It covers a vast selection of topics related to color and its reproduction, all in a very readable form.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/color-spaces/#final-words)

Many of the concepts we’ve discussed were developed decades ago, but despite the age even the old ideas continue to be incredibly useful and the science behind them is expanded to this day.

Color is one of those areas with seemingly infinite depth of complexity. I hopefully showed you that some of that complexity isn’t actually as scary as it looks, you just need to shine a light on it.
