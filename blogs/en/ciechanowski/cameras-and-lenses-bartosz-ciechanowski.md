---
title: Cameras and Lenses – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/cameras-and-lenses/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4da6f38cba2980aa'
translated: false
---

> 原文：[Cameras and Lenses – Bartosz Ciechanowski](https://ciechanow.ski/cameras-and-lenses/)　·　Bartosz Ciechanowski

# [Cameras and Lenses](https://ciechanow.ski/cameras-and-lenses/)

Pictures have always been a meaningful part of the human experience. From the first cave drawings, to sketches and paintings, to modern photography, we’ve mastered the art of recording what we see.

Cameras and the lenses inside them may seem a little mystifying. In this blog post I’d like to explain not only how they work, but also how adjusting a few tunable parameters can produce fairly different results:

Over the course of this article we’ll build a simple camera from first principles. Our first steps will be very modest – we’ll simply try to take any picture. To do that we need to have a sensor capable of detecting and measuring light that shines onto it.

# Recording Light[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/cameras-and-lenses/#recording-light)

Before the dawn of the digital era, photographs were taken on a piece of film covered in crystals of [silver halide](https://en.wikipedia.org/wiki/Silver_halide). Those compounds are light-sensitive and when exposed to light they form a speck of metallic silver that can later be developed with further chemical processes.

For better or for worse, I’m not going to discuss analog devices – these days most cameras are digital. Before we continue the discussion relating to light we’ll use the classic trick of turning the illumination off. Don’t worry though, we’re not going to stay in darkness for too long.

The [image sensor](https://en.wikipedia.org/wiki/Image_sensor) of a digital camera consists of a grid of photodetectors. A photodetector converts photons into electric current that can be measured – the more photons hitting the detector the higher the signal.

In the demonstration below you can observe how photons fall onto the arrangement of detectors represented by small squares. After some processing, the value read by each detector is converted to the brightness of the resulting image pixels which you can see on the right side. I’m also symbolically showing which _photosite_ was hit with a short highlight. The slider below controls the flow of time:

The longer the time of collection of photons the more of them are hitting the detectors and the brighter the resulting pixels in the image. When we don’t gather enough photons the image is [underexposed](#), but if we allow the photon collection to run for too long the image will be [overexposed](#).

While the photons have the “color” of their [wavelength](https://ciechanow.ski/color-spaces/#and-there-was-light), the photodetectors don’t see that hue – they only measure the total intensity which results in a black and white image. To record the color information we need to separate the incoming photons into distinct groups. We can put tiny color filters on top of the detectors so that they will only accept, more or less, red, green, or blue light:

This [color filter array](https://en.wikipedia.org/wiki/Color_filter_array) can be arranged in many different formations. One of the simplest is a [Bayer filter](https://en.wikipedia.org/wiki/Bayer_filter) which uses one red, one blue, and _two_ green filters arranged in a 2x2 grid:

A Bayer filter uses two green filters because light in green part of the spectrum heavily [correlates](https://en.wikipedia.org/wiki/Luminosity_function) with perceived brightness. If we now repeat this pattern across the entire sensor we’re able to collect color information. For the next demo we will also double the resolution to an astonishing 1 kilopixel arranged in a 32x32 grid:

Note that the individual sensors themselves still only see the intensity, and not the color, but knowing the arrangement of the filters we can recreate the colored intensity of each sensor, as shown on the right side of the simulation.

The final step of obtaining a normal image is called [_demosaicing_](https://en.wikipedia.org/wiki/Demosaicing). During demosaicing we want to reconstruct the full color information by filling in the gaps in the captured RGB values. One of the simplest ways to do it is to just linearly interpolate the values between the existing neighbors. I’m not going to focus on the details of many other available demosaicing algorithms and I’ll just present the resulting image created by the process:

Notice that yet again the overall brightness of the image depends on the length of time for which we let the photons through. That duration is known as [_shutter speed_](https://en.wikipedia.org/wiki/Shutter_speed) or exposure time. For most of this presentation I will ignore the time component and we will simply assume that the shutter speed has been set _just right_ so that the image is well exposed.

The examples we’ve discussed so far were very convenient – we were surrounded by complete darkness with the photons neatly hitting the pixels to form a coherent image. Unfortunately, we can’t count on the photon paths to be as favorable in real environments, so let’s see how the sensor performs in more realistic scenarios.

Over the course of this article we will be taking pictures of this simple scene. The almost white background of this website is also a part of the scenery – it represents a bright overcast sky. You can drag around the demo to see it from other directions:

Let’s try to see what sort of picture would be taken by a sensor that is placed near the objects without any enclosure. I’ll also significantly increase the sensor’s resolution to make the pixels of the final image align with the pixels of your display. In the demonstration below the left side represents a view of the scene with the small greenish sensor present, while the right one shows the taken picture:

This is not a mistake. As you can see, the obtained image doesn’t really resemble anything. To understand why this happens let’s first look at the light radiated from the scene.

If you had a chance to explore how [surfaces reflect light](https://ciechanow.ski/lights-and-shadows/#reflections), you may recall that most matte surfaces scatter the incoming light in every direction. While I’m only showing a few examples, _every_ point on every surface of this scene reflects the photons it receives from the whiteish background light source all around itself:

The red sphere ends up radiating red light, the green sphere radiates green light, and the gray checkerboard floor reflects white light of lesser intensity. Most importantly, however, the light emitted from the background is _also_ visible to the sensor.

The problem with our current approach to taking pictures is that every pixel of the sensor is exposed to the _entire_ environment. Light radiated from every point of the scene and the white background hits every point of the sensor. In the simulation below you can witness how light from different directions hits one point on the surface of the sensor:

Clearly, to obtain a discernible image we have to limit the range of directions that affect a given pixel on the sensor. With that in mind, let’s put the sensor in a box that has a small hole in it. The first slider controls the diameter of the hole, while the second one controls the distance between the opening and the sensor:

While not shown here, the inner sides of the walls are all black so that no light is reflected inside the box. I also put the sensor on the back wall so that the light from the hole shines onto it. We’ve just built a [_pinhole camera_](https://en.wikipedia.org/wiki/Pinhole_camera), let’s see how it performs. Observe what happens to the taken image as we tweak the diameter of the hole with the first slider, or change the distance between the opening and the sensor with the second one:

There are so many interesting things happening here! The most pronounced effect is that the image is inverted. To understand why this happens let’s look at the schematic view of the scene that shows the light rays radiated from the objects, going through the hole, and hitting the sensor:

As you can see the rays cross over in the hole and the formed image is a horizontal and a vertical reflection of the actual scene. Those two flips end up forming a 180° rotation. Since rotated images aren’t convenient to look at, all cameras automatically rotate the image for presentation and for the rest of this article I will do so as well.

When we change the distance between the hole and the sensor the viewing angle changes drastically. If we trace the rays falling on the corner pixels of the sensor we can see that they define the extent of the visible section of the scene:

Rays of light coming from outside of that shape still go through the pinhole, but they land outside of the sensor and aren’t recorded. As the hole moves further away from the sensor, the angle, and thus the [field of view](https://en.wikipedia.org/wiki/Field_of_view) visible to the sensor gets smaller. We can see this in a top-down view of the camera:

Coincidentally, this diagram also helps us explain two other effects. Firstly, in the photograph the red sphere looks almost as big as the green one, even though the scene view shows the latter is much larger. However, both spheres end up occupying roughly [the same span](#) on the sensor and their size in the picture is similar. It’s also worth noting that the spheres seem to grow when the field of view gets narrower because their light covers larger part of the sensor.

Secondly, notice that different pixels of the sensor have different distance and relative orientation to the hole. The pixels right in the center of the sensor see the pinhole straight on, but pixels positioned at an angle to the main axis see a distorted pinhole that is further away. The ellipse in the bottom right corner of the demonstration below shows how a pixel positioned at the blue point sees the pinhole:

This change in the visible area of the hole causes the darkening we see in the corners of the photograph. The value of the _cosine_ of the angle I’ve marked with a yellow color is quite important as it contributes to the reduction of visible light in four different ways:

- Two cosine factors from the increased distance to the hole, it’s essentially the [inverse square law](https://ciechanow.ski/lights-and-shadows/#inverse_square)
- A cosine factor from the side squeeze of the circular hole seen at an angle
- A cosine factor from the relative [tilt of the receptor](https://ciechanow.ski/lights-and-shadows/#cosine_factor)

These four factors conspire together to reduce the illumination by a factor of **cos^4(α)** in what is known as _cosine-fourth-power law_, also described as [natural vignetting](https://en.wikipedia.org/wiki/Vignetting#Natural_vignetting).

Since we know the relative geometry of the camera and the opening we can correct for this effect by simply dividing by the falloff factor and from this point on I will make sure that the images don’t have darkened corners.

The final effect we can observe is that when the hole gets smaller the image gets sharper. Let’s see how the light radiated from two points of the scene ends up going through the camera depending on the diameter of the pinhole:

We can already see that larger hole size ends up creating a bigger spread on the sensor. Let’s see this situation up close on a simple grid of detecting cells. Notice what happens to the size of the final circle hitting the sensor as that diameter of the hole changes:

When the hole is [small enough](#) rays from the source only manage to hit one pixel on the sensor. However, at [larger radii](#) the light spreads onto other pixels and a tiny point in the scene is no longer represented by a single pixel causing the image to no longer be sharp.

It’s worth pointing out that sharpness is ultimately arbitrary – it depends on the size at which the final image is seen, viewing conditions, and visual acuity of the observer. The same photograph that looks sharp on a postage stamp may in fact be very blurry when seen on a big display.

By reducing the size of the cone of light we can make sure that the source light affects a limited number of pixels. Here, however, lays the problem. The sensor we’ve been using so far has been an idealized detector capable of flawless adjustment of its sensitivity to the lighting conditions. If we instead were to fix the sensor sensitivity adjustment, the captured image would look more like this:

As the relative size of the hole visible to the pixels of the sensor gets smaller, be it due to reduced diameter or increased distance, fewer photons hit the surface and the image gets dimmer.

To increase the number of photons we capture we could extend the duration of collection, but increasing the exposure time comes with its own problems – if the photographed object moves or the camera isn’t held steady we risk introducing some [motion blur](https://en.wikipedia.org/wiki/Motion_blur).

Alternatively, we could increase the [sensitivity](https://en.wikipedia.org/wiki/Film_speed) of the sensor which is described using the ISO rating. However, boosting the ISO may introduce a higher level of [noise](https://en.wikipedia.org/wiki/Image_noise). Even with these problems solved an actual image obtained by smaller and smaller holes would actually start getting blurry again due to [diffraction](https://en.wikipedia.org/wiki/Diffraction) effects of light.

If you recall how diffuse surfaces reflect light you may also realize how incredibly inefficient a pinhole camera is. A single point on the surface of an object radiates light into its surrounding hemisphere, however, the pinhole captures only a tiny portion of that light.

More importantly, however, a pinhole camera gives us minimal artistic control over _which_ parts of the picture are blurry. In the demonstration below you can witness how changing which object is in focus heavily affects what is the primary target of attention of the photograph:

Let’s try to build an optical device that would solve both of these problems: we want to find a way to harness a bigger part of the energy radiated by the objects and also control what is blurry and _how_ blurry it is. For the objects in the scene that are supposed to be sharp we want to collect a big chunk of their light and make it converge to the smallest possible point. In essence, we’re looking for an instrument that will do something like this:

We could then put the sensor at the focus point and obtain a sharp image. Naturally, the contraption we’ll try to create has to be transparent so that the light can pass through it and get to the sensor, so let’s begin the investigation by looking at a piece of glass.

# Glass[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/cameras-and-lenses/#glass)

In the demonstration below I put a red stick behind a pane of glass. You can adjust the thickness of this pane with the gray slider below:

When you look at the stick through the surface of a thick glass [straight on](#), everything looks normal. However, as your viewing direction [changes](#) the stick seen through the glass seems out of place. The thicker the glass and the steeper the viewing angle the bigger the offset.

Let’s focus on one point on the surface of the stick and see how the rays of light radiated from its surface propagate through the subsection of the glass. The red slider controls the position of the source and the gray slider controls the thickness. You can drag the demo around to see it from different viewpoints:

For some reason the rays passing through glass at an angle are [deflected off their paths](#). The change of direction happens whenever the ray enters or leaves the glass.

To understand _why_ the light changes direction we have to peek under the covers of [classical electromagnetism](https://en.wikipedia.org/wiki/Classical_electromagnetism) and talk a bit more about waves.

# Waves[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/cameras-and-lenses/#waves)

It’s impossible to talk about wave propagation without involving the time component, so the simulations in this section are animated – you can play and pause them by clickingtapping on the button in their bottom left corner.

By default all animations are enabled, but if you find them distracting, or if you want to save power, you can [globally pause](#) all the following demonstrations.disabled, but if you’d prefer to have things moving as you read you can [globally unpause](#) them and see all the waves oscillating.

Let’s begin by introducing the simplest sinusoidal wave:

A wave like this can be characterized by two components. [Wavelength](https://en.wikipedia.org/wiki/Wavelength) **λ** is the distance over which the shape of the wave repeats. Period **T** defines how much time a full cycle takes.

[Frequency](https://en.wikipedia.org/wiki/Frequency) **f**, is just a reciprocal of period and it’s more commonly used – it defines how many waves per second have passed over some fixed point. Wavelength and frequency define [phase velocity](https://en.wikipedia.org/wiki/Phase_velocity) **v~p** which describes how quickly a point on a wave, e.g. a peak, moves:

v~p = λ · f

The sinusoidal wave is the building block of a polarized electromagnetic plane wave. As the name implies electromagnetic radiation is an interplay of oscillations of electric field **E** and magnetic field **B**:

In an electromagnetic wave the magnetic field is tied to the electric field so I’m going to hide the former and just visualize the latter. Observe what happens to the electric component of the field as it passes through a block of glass. I need to note that dimensions of wavelengths are _not_ to scale:

Notice that the wave remains continuous at the boundary and inside the glass the frequency of the passing wave remains constant, However, the wavelength and thus the phase velocity are reduced – you can see it clearly [from the side](#).

The microscopic reason for the phase velocity change is [quite complicated](https://en.wikipedia.org/wiki/Ewald%E2%80%93Oseen_extinction_theorem), but it can be quantified using the [_index of refraction_](https://en.wikipedia.org/wiki/Refractive_index) **n**, which is the ratio of the speed of light **c** to the phase velocity **v~p** of lightwave in that medium:

n = c / v~p

The higher the index of refraction the _slower_ light propagates through the medium. In the table below I’ve presented a few different indices of refraction for some materials:

| vacuum | 1.00 |
|---|---|
| air | 1.0003 |
| water | 1.33 |
| glass | 1.53 |
| diamond | 2.43 |

Light traveling through air barely slows down, but in a diamond it’s over twice as slow. Now that we understand how index of refraction affects the wavelength in the glass, let’s see what happens when we change the direction of the incoming wave:

The wave in the glass has a shorter wavelength, but it still has to match the positions of its peaks and valleys across the boundary. As such, the direction of propagation [must change](#) to ensure that continuity.

I need to note that the previous two demonstrations presented a two dimensional wave since that allowed me to show the sinusoidal component oscillating into the third dimension. In real world the lightwaves are three dimensional and I can’t really visualize the sinusoidal component without using the fourth dimension which has [its own set of complications](https://ciechanow.ski/tesseract/).

The alternative way of presenting waves is to use [_wavefronts_](https://en.wikipedia.org/wiki/Wavefront). Wavefronts connect the points of the same phase of the wave, e.g. all the peaks or valleys. In two dimensions wavefronts are represented by lines:

In three dimensions the wavefronts are represented by _surfaces_. In the demonstration below a single source emits a spherical wave, points of the same phase in the wave are represented by the moving shells:

By drawing lines that are perpendicular to the surface of the wavefront we create the familiar rays. In this interpretation rays simply show the local direction of wave propagation which can be seen in this example of a section of a spherical 3D wave:

I will continue to use the ray analogy to quantify the change in direction of light passing through materials. The relation between the angle of incidence **θ~1** and angle of refraction **θ~2** can be formalized with the equation known as [Snell’s law](https://en.wikipedia.org/wiki/Snell%27s_law):

n~1 · sin(θ~1) = n~2 · sin(θ~2)

It describes how a ray of light changes direction relative to the surface normal on the border between two different media. Let’s see it in action:

When traveling from a less to more refractive material the ray bends [_towards_ the normal](#), but when the ray exits the object with higher index of refraction it bends [_away_ from the normal](#).

Notice that in [some configurations](#) the refracted ray completely disappears, however, this doesn’t paint a full picture because we’re currently completely ignoring reflections.

All transparent objects reflect some amount of light. You may have noticed that reflection on a surface of a calm lake or even on the other side of the glass demonstration at the beginning of the [previous section](#glass). The intensity of that reflection depends on the index of refraction of the material and the angle of the incident ray. Here’s a more realistic demonstration of how light would get refracted _and_ reflected between two media:

The relation between _transmittance_ and _reflectance_ is determined by [Fresnel equations](https://en.wikipedia.org/wiki/Fresnel_equations). Observe that the curious case of missing light that we saw previously [no longer occurs](#) – that light is actually reflected. The transition from partial reflection and refraction to the complete reflection is continuous, but near the end it’s very rapid and at some point the refraction [completely disappears](#) in the effect known as [total internal reflection](https://en.wikipedia.org/wiki/Total_internal_reflection).

The [_critical angle_](https://en.wikipedia.org/wiki/Total_internal_reflection#Critical_angle) at which the total internal reflection starts to happen depends on the indices of refraction of the boundary materials. Since that coefficient is low for air, but very high for diamond a [proper cut](https://en.wikipedia.org/wiki/Brilliant_(diamond_cut)) of the faces [makes diamonds](https://physics.stackexchange.com/questions/43361/why-do-diamonds-shine/43373#43373) very shiny.

While interesting on its own, reflection in glass isn’t very relevant to our discussion and for the rest of this article we’re not going to pay much attention to it. Instead, we’ll simply assume that the materials we’re using are covered with high quality [anti-reflective coating](https://en.wikipedia.org/wiki/Anti-reflective_coating).

# Manipulating Rays[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/cameras-and-lenses/#manipulating-rays)

Let’s go back to the example that started the discussion of light and glass. When both sides of a piece of glass are parallel, the ray is shifted, but it still travels in the same direction. Observe what happens to the ray when we change the relative angle of the surfaces of the glass.

When we make two surfaces of the glass _not_ parallel we gain the ability to change the direction of the rays. Recall, that we’re trying to make the rays hitting the optical device _converge_ at a certain point. To do that we have to bend the rays in the upper part down and, conversely, bend the rays in the lower part up.

Let’s see what happens if we shape the glass to have different angles between its walls at different height. In the demonstration below you can control how many distinct segments a piece of glass is shaped to:

As the number of segments [approaches infinity](#) we end up with a continuous surface without any edges. If we look at the crossover point [from the side](#) you may notice that we’ve managed to converge the rays across one axis, but the top-down view [reveals](#) that we’re not done yet. To focus all the rays we need to replicate that smooth shape across _all_ possible directions – we need rotational symmetry:

We’ve created a _convex_ [thin lens](https://en.wikipedia.org/wiki/Thin_lens). This lens is idealized, in the later part of the article we’ll discuss how real lenses aren’t as perfect, but for now it will serve us very well. Let’s see what happens to the focus point when we change the position of the red source:

When the source is positioned [very far away](#) the incoming rays become parallel and after passing through lens they converge at a certain distance away from the center. That distance is known as [_focal length_](https://en.wikipedia.org/wiki/Focal_length).

The previous demonstration also shows two more general distances: **s~o** which is the distance between the **o**bject, or source, and the lens, as well as **s~i** which is the distance between the **i**mage and the lens. These two values and the focal length **f** are related by the [_thin lens equation_](https://en.wikipedia.org/wiki/Thin_lens#Image_formation):

1 / s~o  + 1 / s~i  = 1 / f

Focal length of a lens depends on both the index of refraction of the material from which the lens is made and its shape:

Now that we understand how a simple convex lens works we’re ready to mount it into the hole of our camera. We will still control the distance between the sensor and the lens, but instead of controlling the diameter of the lens we’ll instead control its focal length:

When you look at the lens [from the side](#) you may observe how the focal length change is tied to the shape of the lens. Let’s see how this new camera works in action:

Once again, a lot of things are going on here! Firstly, let’s try to understand how the image is formed in the first place. The demonstration below shows paths of rays from two separate points in the scene. After going through the lens they end up hitting the sensor:

Naturally, this process happens for _every_ single point in the scene which creates the final image. Similarly to a pinhole a convex lens creates an inverted picture – I’m still correcting for this by showing you a rotated photograph.

Secondly, notice that the distance between the lens and the sensor still controls the field of view. As a reminder, the focal length of a lens simply defines the distance from the lens at which the rays coming from infinity converge. To achieve a sharp image, the sensor has to be placed at the location where the rays focus and _that’s_ what’s causing the field of view to change.

In the demonstration below I’ve visualized how rays from a very far object focus through a lens of adjustable focal length, notice that to obtain a sharp image we must change the distance between the lens and the sensor which in turn causes the field of view to change:

If we want to change the object on which a camera with a lens of a fixed focal length is focused, we have to move the image plane closer or further away from the lens which affects the angle of view. This effect is called [focus breathing](https://en.wikipedia.org/wiki/Breathing_(lens)):

A lens with a fixed focal length like the one above is often called a _prime_ lens, while lenses with adjustable focal length are called _zoom_ lenses. While the lenses in our eyes do dynamically adjust their focal lengths by changing their shape, rigid glass can’t do that so zoom lenses use a system of multiple glass elements that change their relative position to achieve this effect.

In the simulation above notice the difference in sharpness between the red and green spheres. To understand why this happens let’s analyze the rays emitted from two points on the surface of the spheres. In the demonstration below the right side shows the light seen by the sensor _just_ from the two marked points on the spheres:

The light from the point in focus converges to a point, while the light from an out-of-focus point spreads onto a circle. For larger objects the multitude of overlapping out-of-focus circles creates a smooth blur called [_bokeh_](https://en.wikipedia.org/wiki/Bokeh). With tiny and bright light sources that circle itself is often visible, you may have seen effects like the one in the demonstration below in some photographs captured in darker environments:

Notice that the circular shape is visible for lights both in front of and behind the focused distance. As the object is positioned closer or further away from the lens the image plane “slices” the cone of light at different location:

That circular spot is called a [_circle of confusion_](https://en.wikipedia.org/wiki/Circle_of_confusion). While in many circumstances the blurriness of the background or the foreground looks very appealing, it would be very useful to control how much blur there is.

Unfortunately, we don’t have total freedom here – we still want the primary photographed object to remain in focus so its light has to converge to a point. We just want to change the size of the circle of out-of-focus objects without moving the central point. We can accomplish that by changing the _angle_ of the cone of light:

There are two methods we can use to modify that angle. Firstly, we can change the focal length of the lens – you may recall that with longer focal lengths the cone of light also gets longer. However, changing the focal length and keeping the primary object in focus requires moving the image plane which in turn changes how the picture is framed.

The alternative way of reducing the angle of the cone of light is to simply ignore some of the “outer” rays. We can achieve that by introducing a stop with a hole in the path of light:

This hole is called an [_aperture_](https://en.wikipedia.org/wiki/Aperture). In fact, even the hole in which the lens is mounted is an aperture of some sort, but what we’re introducing is an _adjustable_ aperture:

Let’s try to see how an aperture affects the photographs taken with our camera:

In real camera lenses an adjustable aperture is often constructed from a set of overlapping blades that constitute an _iris_. The movement of those blades changes the size of the aperture:

The shape of the aperture also defines the shape of bokeh. This is the reason why bokeh sometimes has a polygonal shape – it’s simply the shape of the “cone” of light after passing through the blades of the aperture. Next time you watch a movie pay a close attention to the shape of out-of-focus highlights, they’re often polygonal:

As the aperture diameter decreases, larger and larger areas of the photographed scene remain sharp. The term [_depth of field_](https://en.wikipedia.org/wiki/Depth_of_field) is used to define the length of the region over which the objects are acceptably sharp. When describing the depth of field we’re trying to conceptually demark those two boundary planes and see how far apart they are from each other.

Let’s see the depth of field in action. The black slider controls the aperture, the blue slider controls the focal length, and the red slider changes the position of the object relative to the camera. The **green dot** shows the place of perfect focus, while the **dark blue dots** show the limits, or the depth, of positions between which the image of the red light source will be reasonably sharp, as shown by a single outlined pixel on the sensor:

Notice that [the larger](#) the diameter of aperture and [the shorter](#) the focal length the shorter the distance between the **dark blue dots** and thus the _shallower_ the depth of field becomes. If you recall our discussion of sharpness this demonstration should make it easier to understand why reducing the angle of the cone _increases_ the depth of field.

If you don’t have perfect vision you may have noticed that squinting your eyes makes you see things a little better. Your eyelids covering some part of your iris simply act as an aperture that decreases the angle of the cone of light falling into your eyes making things slightly less blurry on your retina.

An interesting observation is that aperture defines the diameter of the base of the captured cone of light that is emitted from the object. Twice as large aperture diameter captures roughly _four_ times more light due to increased [solid angle](https://ciechanow.ski/lights-and-shadows/#solid-angles). In practice, the actual size of the aperture as seen from the point of view of the scene, or the [_entrance pupil_](https://en.wikipedia.org/wiki/Entrance_pupil), depends on all the lenses in front of it as the shaped glass may scale the perceived size of the aperture.

On the other hand, when a lens is focused correctly, the focal length defines how large a source object is in the picture. By doubling the focal length we double the width _and_ the height of the object on the sensor thus increasing the area by the factor of four. The light from the source is more spread out and each individual pixel receives less light.

The total amount of light hitting each pixel is proportional to the _ratio_ between the focal length **f** and the diameter of the entrance pupil **D**. This ratio is known as the [_f-number_](https://en.wikipedia.org/wiki/F-number):

N = f / D

A lens with a focal length of 50 mm and the entrance pupil of 25 mm would have **N** equal to 2 and the _f_-number would be known as _f_/2. Since the amount of light getting to each pixel of the sensor increases with the diameter of the aperture and decreases with the focal length, the _f_-number controls the brightness of the projected image.

The _f_-number with which commercial lenses are marked usually defines the maximum aperture a lens can achieve and the smaller the _f_-number the more light the lens passes through. Bigger amount of incoming light allows reduction of exposure time, so the smaller the _f_-number the [_faster_](https://en.wikipedia.org/wiki/Lens_speed) the lens is. By reducing the size of the aperture we can modify the _f_-number with which a picture is taken.

The _f_-numbers are often multiples of 1.4 which is an approximation of 2. Scaling the diameter of an adjustable aperture by 2 scales its _area_ by 2 which is a convenient factor to use. Increasing the _f_-number by a so-called [_stop_](https://en.wikipedia.org/wiki/F-number#Stops,_f-stop_conventions,_and_exposure) halves the amount of received light. The demonstration below shows the relative sizes of the aperture through which light is being seen:

To maintain the overall brightness of the image when [stopping down](https://en.wikipedia.org/wiki/Stopping_down) we’d have to either increase the exposure time or the sensitivity of the sensor.

While aperture settings let us easily control the depth of field, that change comes at a cost. When the _f_-number increases and the aperture diameter gets smaller we effectively start approaching a pinhole camera with all its related complications.

In the final part of this article we will discuss the entire spectrum of another class of problems that we’ve been conveniently avoiding all this time.

# Aberrations[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/cameras-and-lenses/#aberrations)

In our examples so far we’ve been using a perfect idealized lens that did exactly what we want and in all the demonstrations I’ve relied on a certain simplification known as the [paraxial approximation](https://en.wikipedia.org/wiki/Paraxial_approximation). However, the physical world is a bit more complicated.

The most common types of lenses are _spherical_ lenses – their curved surfaces are sections of spheres of different radii. These types of lenses are easier to manufacture, however, they actually don’t perfectly converge the rays of incoming light. In the demonstration below you can observe how fuzzy the focus point is for various lens radii:

This imperfection is known as [_spherical aberration_](https://en.wikipedia.org/wiki/Spherical_aberration). This specific flaw can be corrected with [_aspheric lenses_](https://en.wikipedia.org/wiki/Aspheric_lens), but unfortunately there are other types of problems that may not be easily solved by a single lens. In general, for monochromatic light there are five primary types of aberrations: [spherical aberration](https://en.wikipedia.org/wiki/Spherical_aberration), [coma](https://en.wikipedia.org/wiki/Coma_(optics)), [astigmatism](https://en.wikipedia.org/wiki/Astigmatism_(optical_systems)), [field curvature](https://en.wikipedia.org/wiki/Petzval_field_curvature), and [distortion](https://en.wikipedia.org/wiki/Distortion_(optics)).

We’re still not out of the woods even if we manage to minimize these problems. In normal environments light is very _non_-monochromatic and nature sets another hurdle into optical system design. Let’s quickly go back to the dark environment as we’ll be discussing a single beam of white light.

Observe what happens to that beam when it hits a piece of glass. You can make the sides non-parallel by using the slider:

What we perceive as white light is a combination of lights of different wavelengths. In fact, the index of refraction of materials _depends_ on the wavelength of the light. This phenomenon called [_dispersion_](https://en.wikipedia.org/wiki/Dispersion_(optics)) splits what seems to be a uniform beam of white light into a fan of color bands. The very same mechanism that we see here is also responsible for a rainbow.

In a lens this causes different wavelengths of light to focus at different offsets – the effect known as [_chromatic aberration_](https://en.wikipedia.org/wiki/Chromatic_aberration). We can easily visualize the _axial_ chromatic aberration even on a lens with spherical aberration fixed. I’ll only use red, green, and blue dispersed rays to make things less crowded, but remember that other colors of the spectrum are present in between. Using the slider you can control the amount of dispersion the lens material introduces:

Chromatic aberration may be corrected with an [achromatic lens](https://en.wikipedia.org/wiki/Achromatic_lens), usually in the form of a [doublet](https://en.wikipedia.org/wiki/Doublet_(lens)) with two different types of glass fused together.

To minimize the impact of the aberrations, camera lenses use more than one optical element on their pathways. In this article I’ve only shown you simple lens systems, but a high-end camera lens may consist of [a lot of elements](https://en.wikipedia.org/wiki/File:Objective_Zeiss_Cut.jpg) that were carefully designed to balance the optical performance, weight, and cost.

While we, in our world of computer simulations on this website, can maintain the illusion of simple and perfect systems devoid of aberrations, [vignetting](https://en.wikipedia.org/wiki/Vignetting), and [lens flares](https://en.wikipedia.org/wiki/Lens_flare), real cameras and lenses have to deal with all these problems to make the final pictures look good.

# Further Watching and Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/cameras-and-lenses/#further-watching-and-reading)

Over on YouTube [Filmmaker IQ channel](https://www.youtube.com/channel/UCSFAYalJ2Q7Tm_WmLgetmeg) has a lot of great content related to lenses and movie making. Two videos especially fitting here are [The History and Science of Lenses](https://www.youtube.com/watch?v=1YIvvXxsR5Y) and [Focusing on Depth of Field and Lens Equivalents](https://www.youtube.com/watch?v=lte9pa3RtUk).

[What Makes Cinema Lenses So Special!?](https://www.youtube.com/watch?v=q1n2DR6H7mk) on [Potato Jet channel](https://www.youtube.com/channel/UCNJe8uQhM2G4jJFRWiM89Wg) is a great interview with Art Adams from [ARRI](https://www.arri.com/en/). The video goes over many interesting details of high-end cinema lens design, for example, how the lenses [compensate for focus breathing](https://youtu.be/q1n2DR6H7mk?t=370), or how much attention is paid to the [quality of bokeh](https://youtu.be/q1n2DR6H7mk?t=899).

For a deeper dive on bokeh itself Jakub Trávník’s [On Bokeh](https://jtra.cz/stuff/essays/bokeh/index.html) is a great article on the subject. The author explains how aberrations may cause bokeh of non uniform intensity and shows many photographs of real cameras and lenses.

In this article I’ve mostly been using [geometrical optics](https://en.wikipedia.org/wiki/Geometrical_optics) with some soft touches of electromagnetism. For a more modern look at the nature of light and its interaction with matter I recommend Richard Feynman’s [QED: The Strange Theory of Light and Matter](https://en.wikipedia.org/wiki/QED:_The_Strange_Theory_of_Light_and_Matter). The book is written in a very approachable style suited for general audience, but it still lets Feynman’s wits and brilliance shine right through.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/cameras-and-lenses/#final-words)

We’ve barely scratched the surface of optics and camera lens design, but even the most complex systems end up serving the same purpose: to tell light where to go. In some sense optical engineering is all about taming the nature of light.

The simple act of pressing the shutter button in a camera app on a smartphone or on the body of a high-end DSLR is effortless, but it’s at this moment when, through carefully guided rays hitting an array of photodetectors, we immortalize reality by painting with light.
