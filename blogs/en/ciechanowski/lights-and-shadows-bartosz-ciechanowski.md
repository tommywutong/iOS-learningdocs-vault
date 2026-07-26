---
title: Lights and Shadows – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/lights-and-shadows/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:c78f9a19c6d621c4'
translated: false
---

> 原文：[Lights and Shadows – Bartosz Ciechanowski](https://ciechanow.ski/lights-and-shadows/)　·　Bartosz Ciechanowski

# [Lights and Shadows](https://ciechanow.ski/lights-and-shadows/)

It’s hard to describe how paramount light is. Ultimately, it is the only thing we see. But just as important the presence of light is, so is its absence. To talk about light we have to start in darkness so let’s jump straight into it.

Light is a visible portion of [electromagnetic radiation](https://en.wikipedia.org/wiki/Electromagnetic_radiation), but in this article I’m not going to discuss any of the underlying details like [wave-particle duality](https://en.wikipedia.org/wiki/Wave%E2%80%93particle_duality). Instead, I’ll try to explain how light creates so many beautiful effects seen in everyday life. In the demonstration below you can use the sliders to control the position and size of a rectangular light source. You can also drag around the scene to see it from different angles:

By the end of this article the effects of light in this demonstration should become more clear, but before we get there we have to take a few steps back and start with a much simpler setup.

# Power[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#power)

Let’s begin by introducing a single spherical light source. While this ball of light is not very exciting, you can at least control its brightness with the slider below:

What this slider actually regulates is the _power_ of the light source – the amount of energy emitted from it per second. That energy comes out in a form of [photons](https://en.wikipedia.org/wiki/Photon) which we can crudely represent with rays of light coming out of the source. The higher the power the more rays emitted from the source in a unit of time:

Unfortunately, this demonstration is quite limited. The number of photons per second emitted by even a simple light bulb is absolutely enormous and there is no fixed set of directions in which they travel. Having said that, the ray analogy will be useful for explaining quite a few phenomena, so despite its flaws, it will serve us as a valuable tool.

The power of a light source is measured using the unit of watts **W**. Let’s see how we perceive the brightness of some source depending on its power:

Notice that relative change in the perceived brightness strongly depends on the position of the slider. A change from [5 W](#) to [10 W](#) is much more perceptible than a change from [85 W](#) to [90 W](#). The human visual system has a non-linear response to the power of the incoming light, so a fixed increase in power will not have a fixed increase in perceived brightness.

Additionally, the brightness of the light itself quickly [saturates to pure white](#). We hit the limit of what’s easily presentable with web technologies. There are [ways](https://en.wikipedia.org/wiki/Tone_mapping) to mitigate that problem, but in this article I want to present unmodified levels of brightness as this makes relative comparisons possible.

Despite the white saturation, once we put a matte surface next to a bright light we can easily observe the _effects_ of the increased power. You can drag around the demo to see the scene from a different point of view:

While on its own the surface doesn’t emit any light, it _reflects_ the light emitted from the source. Some part of that reflected light goes straight to our eyes allowing us to see the object. Naturally, the other side of the surface is pitch black – no light gets to it since it’s blocked by the front side.

It may seem trivial to mention these concepts, but reflected and blocked light will end up defining almost everything I’ll discuss in this article.

# Position[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#position)

If you looked closely at the previous simulation you may have noticed that the surface wasn’t uniformly lit. Let’s investigate that variation in shading by moving the light around. In the demonstration below you can control its [altitude angle](https://en.wikipedia.org/wiki/Horizontal_coordinate_system) and distance:

Even with this simple example we can observe that both the angle at which the light is positioned and its distance to the lit object have an impact on the way that matte surface looks. We can try to understand what’s going on by visualizing the rays emitted by the source. To make things easier to see, only the rays that hit the surface are drawn with full length:

Changing the position of the light changes the numbers of rays hitting the surface which affects how the surface looks. Notice that different parts of the surface get different number of rays, so let’s isolate a small area and look at it up close.

First, let’s analyze the impact of altitude angle. In the simulation below a red dot terminates a ray that used to hit the tiny patch in the perpendicular case, but it no longer does so after tilting:

As soon as the light source slants away from the perpendicular direction some of the rays that used to hit the patch no longer do. We can see this situation even better from a side view. The blue arrow shows the surface normal. Similarly to the [two dimensional](https://ciechanow.ski/gears/#tangent-normal) case, a normal direction in three dimensions is locally perpendicular to the surface. The yellow arrow points towards the light source:

As the angle increases, a smaller portion of the original stream of light hits the surface. With the power of the source **P**, the received power _per unit area_ **E** known as [_irradiance_](https://en.wikipedia.org/wiki/Irradiance) that hits the tiny patch of the surface with area **A** is proportional to the _cosine_ of the angle of incidence **α** between the to-light direction and the patch’s normal vector:

E = P · cos(α) / A

For a flat matte surface with small but distant light source the shading results from this _cosine factor_ aren’t particularly exciting, because every point of the surface looks almost the same. However, when every element of the surface has a different angle of incidence, like in the case of a sphere, the shading of a matte surface can look quite pretty. In the example below the yellow arrow shows the direction towards a distant light source:

With the cosine factor covered we can now analyze how the _distance_ to the light source affects the distribution of rays. Yet again, red dots show the intersections of rays that used to hit the patch, but due to increased distance of the light they no longer do so:

The further away the light the fewer photons hit the patch of the surface. For a tiny light source like that we can quantify this relation using geometrical reasoning. In the demonstration below you can witness the rays of light emitted from a small light source in _all_ directions. That source is surrounded by a sphere – you can control its radius with a slider:

Notice, that when the radius of the sphere increases, the density of the yellow intersection points _decreases_. While the number of rays is constant, the total area of the surface increases and the local intensity of light is more diluted. The area of a sphere is proportional to the square of its radius **r**:

A = 4πr^2

As such, received power per unit area **E**, is, with fixed power, proportional to the _inverse_ of the square of the distance **r**:

E = P / A  ~ 1 / r^2

This rule is known as the [inverse square law](https://en.wikipedia.org/wiki/Inverse-square_law) and it holds _accurately_ only for infinitely small light sources, which don’t exist in the physical world. As a result, that simplifying assumption won’t let us explain the variety of shading obtained by even a simple rectangular light source:

To understand what’s going on here we need to change pace a little and discuss angles and fields of views.

# Angles[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#angles)

If you’ve ever looked at a car that was driving away you’ve likely noticed that it seemed smaller as it moved away. In the demonstration below we can recreate this situation by controlling the car’s position. The upper part shows the top-down view of that scene, while the lower part shows how it would appear to your eyes if you were standing on the red dot:

The gray circle around the red dot symbolizes a full surrounding field of view. As the car moves away the angle it _subtends_ in that field of view, as shown by the yellow arc, gets smaller and for this reason the car _appears_ smaller.

# Radians[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#radians)

The car simulation displayed the angle using the unit of degrees, but observe that the length of the yellow arc also gets smaller as the angle gets smaller. In math it’s very common to measure angles as the ratio of the arc’s length to the radius of the circle on which that arc is spanned:

angle = arc length / radius

That measure of an angle is expressed in [radians](https://en.wikipedia.org/wiki/Radian). You can see how degrees and radians relate to each other in the demonstration below:

When an angle measures [1 radian](#), the length of the yellow arc is equal to the length of the blue radius. A circle’s circumference is equal to 2π times the radius so _half_ a full turn measures just [π radians](#).

Similarly to degrees, the measure of angles in radians is completely agnostic to the circle’s radius. The _ratio_ of a circle’s circumference to its radius is always equal to 2π and the ratio of arc’s length to the arc’s radius is just some fraction of that 2π.

As a final consideration in this section let’s investigate what happens to the subtended angle, and thus the arc length, when the object is already small in the field of view and it moves away from the observer:

Notice that the yellow arc is very flat and in this scenario when the object moves twice as far, the angle it subtends gets pretty much twice as small. This follows from a basic proportion of similar triangles when we think of the arc as a straight segment. That approximation becomes more accurate as the arc gets shorter since the curvature becomes even more negligible.

# Solid Angles[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#solid-angles)

In the car example I’ve conveniently focused only on the perceived width of the car, but you’ve probably noticed that the distant vehicle seems to get shorter too. Human vision isn’t just limited to horizontal direction, so let’s try to model our field of view by extending the example into the third dimension. This time, to spare myself a 3D modeling exercise, I’ll use a simple rectangle:

Notice that as the rectangle moves away, the projected _area_ on the sphere gets smaller. This completes the explanation of why objects seem smaller when they are distant – they simply occupy a smaller part of our visual field.

In two dimensions we defined an angle as a ratio of the length of an arc of a circle to that circle’s radius. In three dimensions we similarly define a [_solid angle_](https://en.wikipedia.org/wiki/Solid_angle) to be the ratio of the _area_ of a subtended patch on a sphere to that sphere’s radius squared:

solid angle = patch area / radius^2

The shape of the patch can be completely arbitrary, all that matters is its area. In the demonstration below you can see some solid angles which are measured in _steradians_. I highlighted the cone reaching the patch to make things more visible, but ultimately it’s just the yellow area that defines the solid angle:

Since the area of the sphere is 4π times the radius squared the maximum solid angle is [4π steradians](#). Note that both radian and steradian are dimensionless, we just give them convenient names to recognize that we are talking about angles.

On a final note, let’s look what happens to a small solid angle as the object moves away:

When the projection of the rectangle is small enough the curved patch on the hemisphere can be approximated with a flat piece. Since both the projected width and height are inversely proportional to the distance, the _area_ of the patch shrinks with a _square_ of the distance, in some sense recreating the inverse square law from the point of view of the observer.

# Surface Vision[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#surface-vision)

Let’s try to map the concepts of fields of views and solid angles to the surface from the previous scene. Here it is again:

Every point of the surface is exposed to its environment, but a point can only see its surroundings through a _hemisphere_ centered around it. The other half of the sphere is just blocked by the surface itself – no light can arrive from under it. If we now put the light in the scene and try to project it onto the hemisphere we can observe what’s going on with the projected area. I made the backside of the floor look transparent to let you see the hemisphere from the inside:

The smaller the area, the smaller the solid angle of the light source and thus the smaller amount of light getting to the surface. However, we’re still not accounting for the cosine factor – the solid angles closer to the horizon should be less influential.

It turns out we can fix this problem by employing a simple trick of projecting the outline of the subtended angle from the hemisphere onto the base:

This process automatically accounts for the cosine factor – notice that the projected yellow area on the surface gets smaller when the light source is close to the horizon. This method of a projected solid angle explains how bright a point on a matte surface will appear when lit by a uniform light source.

# Radiance[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#radiance)

What I’ve shown you so far may seem reasonable, but you may wonder about some inconsistencies. As we’ve seen, a matte surface gets dimmer as it moves away from the light and it also gets dimmer as the light’s altitude angle tilts away from the perpendicular direction.

However, the light source itself doesn’t seem to undergo the same effects – it remains consistently bright even as we look at it from an oblique angle or move away from it with a slider:

A matte surface seems to collect the surrounding light from every direction. The human eye and digital cameras work quite differently. Through the optical system, each of the receptors in a retina, or each of the pixels in a camera, collects light only from a very small solid angle. In the demonstration below a tiny blue receptor on the left is exposed only to the light “seen” by the yellow cone:

As the light source moves away, the power reaching the receptor is reduced by the inverse of the square of a distance. However, at the same time the amount of light’s surface visible to the solid angle _increases_ by a square of distance – you can observe the circle of the cone’s base in the bottom right corner. These two effects cancel each other out and the perceived brightness remains constant.

Receptors like these measure [_radiance_](https://en.wikipedia.org/wiki/Radiance) which is power per unit area _and_ per unit solid angle. Both the size of the receptor _and_ the solid angle from which it receives the light contribute to the amount of collected energy.

When the light is seen by a person we often use the term [_luminance_](https://en.wikipedia.org/wiki/Luminance), which is just radiance weighted by [wavelength sensitivity function](https://en.wikipedia.org/wiki/Luminosity_function) of the human visual system. Luminance defines how bright an object appears to our eyes and it’s expressed in [nits](https://en.wikipedia.org/wiki/Candela_per_square_metre) – you may have heard that term referring to a display’s brightness.

The viewing _angle_ independence of light sources applies only to so called Lambertian emitters, however, many of the typical light sources like frosted light bulbs and the Sun are a close approximation of these idealized generators.

Every point of a Lambertian emitter emits light in the following spherical pattern, the length of an arrow corresponds to relative number of photons per second emitted in the arrow’s direction:

The lengths of the vectors are proportional to the cosine of the angle away from the normal which ends up forming a perfect sphere. To see how this distribution affects the total brightness let’s look at how an observer perceives the light’s surface as seen from a side view:

The yellow shape represents a solid angle from which the receptor receives the light, only the photons emitted directly in its direction will get to it.

As the viewing angle tilts, the length of each arrow gets smaller, so each point of the surface contributes fewer photons towards the observer. However, at the same time the receptor sees a bigger chunk of the surface. The effect of shorter arrows is counterweighted by _more_ arrows being seen.

Since the length of the arrows is proportional to the cosine of the angle and the visible area is _inversely_ proportional to the cosine of the very same angle the total perceived brightness remains constant.

# Reflections[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#reflections)

Eyes and matte surfaces accumulate light differently so this explains why a moving light source affects them differently. The hemispherical model of light aggregation seems to work well for a matte surface, but it certainly doesn’t explain the behavior of a plain mirror:

Let’s try to visualize how a ray of incoming light, represented with a blue arrow, ends up being reflected by the mirror in the direction of a red arrow:

Notice that you’ll only see the reflection of the light source in a place pointed to by an incoming ray if the outgoing ray points [directly at you](#). The way a mirror looks depends on the position of the observer – the same point on its surface may have a very different appearance.

Let’s consider a slightly rougher mirror, one that perhaps wasn’t polished that well. It may reflect light in a pattern similar to this:

Notice how the edges of the reflected light in this material are slightly fuzzier. The lengths of arrows represent radiance and a rougher surface will scatter some amount of light into directions that aren’t exactly aligned with the perfect reflection.

The previous visualization was very light centric since we investigated how the incoming light is scattered into outgoing light, however, we can also try to invert the situation and examine how a single _fixed_ direction of the _outgoing_ light is affected by the incoming light coming from various directions:

When you [position the light](#) slightly off-center of the bulk of the incoming rays and you [look directly](#) at the outgoing direction, you’ll notice that the reflection in that place is indeed less bright because not all of the incoming directions that affect the viewing direction intersect with the light source.

Finally, let’s consider a _Lambertian surface_, which describes a perfectly matte, diffusing material:

Every point of a Lambertian surface just emits a uniform radiance around it. At fixed distance only the cosine factor affects how bright the point is. Effectively, each point of a Lambertian surface acts as a Lambertian emitter – it looks exactly the same from every direction we look at it.

If we analyze how incoming radiance affects outgoing radiance in a single direction we’ll end up with a distribution like this:

This distribution is completely agnostic to the outgoing direction and it actually is exactly equivalent to the hemispherical surface-projected solid angle method we’ve been playing with before – light coming from directions closer to horizon has weaker impact on the final shading.

The way an _arbitrary_ surface reflects light can be significantly more complicated and it is mathematically described with a [certain function](https://en.wikipedia.org/wiki/Bidirectional_reflectance_distribution_function). While there are also more abstract ways to categorize materials e.g. by their roughness, metallicness, or sheen, the general method stands – the outgoing radiance can always be [calculated](https://en.wikipedia.org/wiki/Rendering_equation) as a weighted sum of incoming radiances from all directions.

My primary focus in this article are Lambertian surfaces since they’re a decent model of many real-life materials like matte wall paints and paper. For every viewing direction they’re affected by the light coming from _any_ viewing direction which creates many beautiful shading effects.

# Shadow[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#shadow)

In the demonstration below we face a scene with a familiar rectangular light, but this time I put a black wall in the middle of the floor surface. The wall has a faint outline so that it’s more visible. Using the sliders you can control the source’s altitude angle and size. The total power of light is constant, so that when the source gets smaller its power per area increases – this keeps the scene consistently bright.

There are so many interesting phenomena that we can experience here, for instance, notice that as the light source gets smaller, the shadows it creates get sharper. With our projected hemisphere we can easily see why it happens:

With a [small light source](#) even a small change in position on the surface has big effects on the light’s visibility – it quickly becomes fully visible or fully occluded. On the other hand, with a [big light source](#) that transition is much smoother – the distance on the floor surface between a completely exposed and completely invisible light source is much larger.

Don’t get misled by the microscopic size of the projected area when the source is tiny. Recall that I keep the total power of the source constant, so the power emitted _per area_ is significantly higher for a smaller light and thus even at miniature size it is still very impactful. In this scenario it’s the visible _fraction_ of the total light area that matters.

It’s also worth pointing out that even when the light source is large, the shadow is sharp right at the place where the wall meets the surface since only a tiny step on the floor is required for the light to completely disappear.

# Color[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#color)

So far we’ve been dealing with light sources that emitted white light which was in turn reflected by white surfaces. White light is in fact a combination of many different monochromatic wavelengths. For instance, the spectral distribution of sunlight is [fairly complicated](https://en.wikipedia.org/wiki/Sunlight#/media/File:Solar_spectrum_en.svg). However, nothing prevents us from considering light sources of particular hues:

While pure monochromatic sources of light exist, most of the light we see is some combination of different wavelengths that end up creating a perception of color in our brain. The details of wavelengths, vision, and the way we specify colors deserve [an article on its own](https://ciechanow.ski/color-spaces/) so in here I’ll continue with a little less formal discussion of color.

Light is additive so when a surface is lit by multiple light sources the final shading effect is just a sum of shading effects of all the individual light sources. A white surface lit by both red and blue light will reflect _both_ red and blue light which we perceive as purple:

Note that when some red, green, and blue lights have [equal strength](#) their perfectly even overlap in the center is perceived as a shade of gray which is nothing more than a white light of reduced strength. That color combining property of the human visual system is exploited by various [display technologies](https://en.wikipedia.org/wiki/Pixel#Subpixels).

Colorful light sources aren’t very dramatic without a surface to shine on so in the demonstration below you can change the light’s color and see how it changes the look of these nine tiles. The cyan light is created by a mix of green and blue light:

A tile is of a particular color because it reflects only that part of the spectrum which forms _that_ color while simultaneously absorbing the other parts of light. For example, a green tile absorbs red and blue light, so under white or green light it still looks green. However, that same green tile appears black under red or blue light because it completely absorbs these wavelengths. This substantial dimming effect is actually commonly visible with yellow [sodium lamps](https://en.wikipedia.org/wiki/Sodium-vapor_lamp#/media/File:Red_and_black_cars_under_low_pressure_sodium_lamps.jpg).

It’s important to note that once the light hits the surface the absorbed part of the source’s spectrum is lost – only red light leaves a red tile when lit with a white light. That tile then effectively acts as an emitter of a red light.

# Bounces[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#bounces)

In all the demonstrations so far we’ve only been looking at mostly flat scenes, so let’s build a slightly more complex system consisting of a white floor, a red wall, and a rectangular light source. In the demonstration below you can control the power of that light:

Notice that the red wall doesn’t receive any light from the emitter directly, yet it is visibly lit. Moreover, the back part of the white floor has some reddish hue to it. Each point of a lambertian surface is affected by the light coming from every direction and each point of a lit lambertian surface becomes a light emitter itself. Let’s see how light propagates in the scene by looking at a slice from a side view:

The light reflected from the white floor hits the red wall, which in turn is reflected by the red wall as a red light and it reaches the white floor and so on. In the demonstration below you can see a contribution of each bounce to the final shading in the scene:

With zero bounces we only see the light directly. The first bounce is critical, it provides the initial lighting for the entire rest of the scene – it effectively acts as a light source on its own. After the second bounce the light emitted from the wall is purely red, so once it gets reflected from the white floor in the third bounce it maintains its redness.

This process continues forever, but, thankfully, with each step the amount of the reflected light gets reduced since not all light reflected from a surface falls on the neighboring surface and the surfaces themselves aren’t perfectly reflective – they absorb some part of light. At some point the additional bounces become imperceptible.

# Sphere of Light[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#sphere-of-light)

Let’s go back to our simple scene with just a white floor, but instead of looking at a single light source we’ll add many small ones. In the simulation below a scene is surrounded by a swarm of tiny light sources, you can see their projections onto the hemisphere of the central point:

In limit, if we cover the entire surrounding sphere with tiny light sources it would look like something in the demonstration below. The light covers everything now so we can’t really see the scene anymore, but by dragging the slider you can make the surrounding sphere of light so big that it will start to encompass even you, revealing what’s hidden inside:

For the final part of this article we will remain inside that sphere of light, it will completely surround us and the scenes we will look at. In the demonstration above notice that every point of the surface is now exposed to the entire hemisphere of light with uniform intensity. This removes any differences between the points on the surface – they all receive the same light and end up with the same shading.

You may have seen a situation like that on an overcast day – the Sun isn’t directly visible and the entire sky emits light from every direction. In the last scene of this article let’s see what effects are created when a part of that surrounding light gets occluded. In the demonstration below you can control the position of the black tile and see the shadow it ends up creating:

The closer the black tile is to the gray plane the more light it obscures and the darker the shadow is. We can observe this easily using the hemisphere model. The yellow area represents the projection of the visible light:

This shadow is ultimately no different from the shadows cast by a rectangular wall that we saw before. Shadows are simply the absence of light.

# Further Watching and Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#further-watching-and-reading)

[Physically Based Rendering](https://www.elsevier.com/books/physically-based-rendering/pharr/978-0-12-800645-0) by Matt Pharr, Wenzel Jakob, and Greg Humphreys is _the_ book on creation of photorealistic images with computer graphics. Over the course of the publication authors cover a wide variety of topics related to geometry, color, lights, and materials, while building a full-featured ray tracer at the same time. As of [two years ago](https://pharr.org/matt/blog/2018/10/15/pbr-online.html) the complete book is [available online](http://www.pbr-book.org), for free!

For a shorter overview of a production renderer I recommend [Physically Based Rendering in Filament](https://google.github.io/filament/Filament.html). This documentation provides more rigorous treatment of material properties than what I’ve presented here and it elaborates on many approximating models used in realtime computer graphics.

As the name implies, Vsauce’s [What Is The Speed of Dark?](https://www.youtube.com/watch?v=JTvcpdfGUtQ) discusses an interesting concept of a speed of darkness and it explains how shadows can break the speed of light, thankfully, without breaking the laws of physics.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/lights-and-shadows/#final-words)

It’s truly remarkable that what starts at light sources, what interacts with different objects, and what eventually ends up in our eyes is electromagnetic radiation with different wavelengths and of varying intensity. Math helps us understand _how_ changes to those intensities happen.

With Lambertian surfaces and uniformly bright lights, we can simplify countless interactions of trillions of photons into relatively straightforward geometrical concepts, but even with more complicated materials and light sources, every step of the way can be simulated to create extremely convincing simulations of real life environments.

Naturally, it’s impossible to _completely_ articulate the sheer intricacy and immensity of what spontaneously just happens in the physical world to every photon on a sunny day. Math, however, gives us the tools to raise above that complexity and see the bigger picture.
