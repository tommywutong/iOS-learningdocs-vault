---
title: Earth and Sun – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/earth-and-sun/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f548bd2bddd0b20b'
translated: false
---

> 原文：[Earth and Sun – Bartosz Ciechanowski](https://ciechanow.ski/earth-and-sun/)　·　Bartosz Ciechanowski

# [Earth and Sun](https://ciechanow.ski/earth-and-sun/)

The day-night cycle and the cycle of the seasons have been an important part of human civilization for millennia. Today the [discoveries](https://en.wikipedia.org/wiki/De_revolutionibus_orbium_coelestium) from centuries ago are well known, but despite the superficial simplicity of Earth revolving around its axis and orbiting the Sun, the interaction between those two actually forms a fairly complex system.

This blog post will talk about space and how our planet moves through it, so it’s only fitting if we embed ourselves in the cosmos itself.

Over the course of this article I’ll try to explain how the Sun and the various motions of the Earth end up making our planet look like in the demonstration below. You can drag the globe around to see it from different perspectives and use the sliders to change the date and time:

It’s hard to talk about Earth and Sun without referencing a few dimensions and dates. They’ll be shown in imperialmetric units (e.g. 1 mi1 km) and an Americanan international date format (mm/dd/yyyydd/mm/yyyy), but you can [switch](#) to the more universalAmerican units if you prefer.

The time of day will be presented in [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time), or UTC for short, which is roughly a local time in [Greenwich](https://en.wikipedia.org/wiki/Greenwich) in London, UK. This time standard is _not_ adjusted for daylight saving time which is very convenient as it will let us look at the sunlight for the same time of day at different dates.

# Size[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#size)

Let’s start by visualizing how enormous the Sun is. In the picture below you’ll find the Earth and the Sun placed next to each other. The Earth is the tiny blue dot on the right side of the Sun:

The Sun is almost a perfect sphere with a radius of 432,170 mi695,700 km. The Earth’s shape resembles an [ellipsoid](https://en.wikipedia.org/wiki/Earth_ellipsoid) with an average radius of 3958.8 mi6371 km. As such, the radius of the Sun is 109 times larger than that of the Earth. Naturally, the Sun doesn’t look that large in the sky, but that’s because the Sun is quite far away from the Earth. Before we see how far away the Sun is we first have to discuss a simple shape that is the base of all planetary orbits – an ellipse.

# Ellipse[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#ellipse)

There are multiple ways to define an ellipse, but in the context of space it’s most convenient to speak of it in terms of _focal points_. An ellipse is a figure consisting of points for which the sum of distances to its two focal points is constant. That’s certainly a mouthful, so an interactive diagram will paint a better picture:

The small cross represents the center of an ellipse while the two white disks show its focal points. The total length of blue and red segments is the same for every point on the ellipse. The dashed line is called the semi-major axis of the ellipse while the dotted line is the semi-minor axis.

The defining property of an ellipse is the ratio between a distance c from the center to a focal point known as _linear eccentricity_, and a distance a from the center to the “far point” of the ellipse i.e. the length of its semi-major axis. In the demonstration below you can adjust that ratio with a slider:

This ratio is known as _eccentricity_. When an eccentricity is equal to 0 an ellipse becomes a perfect circle, for eccentricity of 1 an ellipse with a fixed major axis length degenerates into a linear segment.

# Orbit[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#orbit)

You may have already heard that the orbit of the Earth is an ellipse and that the Sun is located in one of the focal points of that ellipse. This situation is often visualized like this:

The small cross in the middle shows the center of the ellipse while the small rings, one of which is directly in the center of the Sun, symbolize the focal points. There are two important points on the orbit: the [perihelion](#) is the point at which Earth is closest to the Sun, while at the [aphelion](#) Earth is the furthest away from the Sun.

Technically, the Sun is _not_ in one of the focal points of the ellipse, but instead the objects in the Solar System revolve around its [center of mass](https://spaceplace.nasa.gov/barycenter/en/). However, the Sun’s mass is so dominant that the actual focal point is [fairly close](https://en.wikipedia.org/wiki/Barycenter#/media/File:Solar_system_barycenter.svg) to the Sun’s center.

What we’ve seen above paints a convenient picture, but the actual relative sizes are very different. Below you’ll find a visualization of the Earth’s orbit around the Sun with proper scales. The tiny yellow dot in the middle depicts the Sun. At your current viewing scale the Earth is pretty much invisible, it has a diameter of  pixels, so instead its location is shown by an arrow. You may also be barely able to tell that the orbit is elliptical. Its eccentricity is equal to 0.0167 and the Sun is very close to the center:

If you pay a close attention to the position of the Earth at the [beginning](#) of a calendar year and compare it with the beginning of the [next year](#) you’ll notice that the Earth hasn’t returned to the exact same position – during 365 days the Earth falls a little short of the full orbit. We’ll soon see that there are multiple ways to define “a day”, but unless stated otherwise we’ll assume that it lasts 24 hours, that is 24 × 60 × 60 = 86400 seconds.

The time it takes Earth to get back to the same point on the orbit is called a [sidereal year](https://en.wikipedia.org/wiki/Sidereal_year) where _sidereal_ means “with respect to stars”. A sidereal year lasts roughly 365.256 days. A sidereal year is actually _not_ the basis of year tracking in civilian time, but we’ll have to wait until the later parts of this article to discuss _the_ period of Earth’s journey around the Sun that defines how we count years.

The eccentricity of the Earth’s orbit is fairly small so the distance between the center of the Sun at aphelion (94,509,460 mi152,098,233 km) is not that much larger than that at perihelion (91,402,640 mi147,098,291 km). As such, the apparent Sun size is only 3.3% smaller when the Sun is the farthest from Earth compared to when it’s closest:

Given the enormous size differences we’re dealing with from this point on I’ll abandon the exact relative dimensions and instead use whatever size is convenient to demonstrate the discussed subject.

# Second Law of Kepler[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#second-law-of-kepler)

An important aspect of planetary motion are [Kepler’s laws](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion) of which the second one describes the planet’s speed at different points on the orbit. In the demonstration below you can make the planet orbit the Sun. As Kepler has discovered, traversal of each of the arc of the pie-slice sections of the orbit takes _the same_ amount of time:

At the bottom part of the simulation you can see the flattened length of the arc the planet sweeps within the same amount of time. When the planet is closer to the Sun it travels a much longer path, that is it moves much _faster_ than when it’s away from the Sun. Kepler’s second law says that the _areas_ of the triangular pieces are the same, so naturally if the height of the triangle is made longer due to a larger distance to the Sun, the base, i.e. the arc swept, has to get shorter to maintain the same area.

For the actual shape of Earth’s orbit the arc length differences are much smaller, but as we’ll discuss, they still impact some aspects of time tracking on Earth.

# Orbital Plane[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#orbital-plane)

So far we’ve been looking at the orbit from above, but a tilted perspective shows that the orbit defines an infinite flat sheet known as the orbital plane. You may drag over the demonstration up and down to change the viewing angle:

In fact, all planets in the Solar System have very similar orbital planes which is a consequence of formation of the planets from a [protoplanetary disk](https://en.wikipedia.org/wiki/Protoplanetary_disk). It’s worth pointing out that the plane represents a _mean_ – Earth wobbles slightly up and down due to changes in position of the Moon, and, to a smaller extent, of other planets.

At this point we’re still not ready to discuss how a year is measured, but understanding the Earth’s revolution around the Sun will actually help us describe the duration of a day, so let’s discuss the most tangible motion of our planet.

# Axial Rotation[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#axial-rotation)

The Earth rotates around its axis from west to east, or, when seen from above, counter-clockwise. In the simulation below you can change the time of day by dragging the slider. The first important thing to observe is that the axis of rotation is not perpendicular to the orbital plane shown as a horizontal line. Currently the axis is tilted at roughly 23.437° away from the vertical:

If you compare the position of the Earth [at the beginning](#) and [at the end](#) of a 24 hour cycle you may notice something surprising – the Earth has completed slightly more than one full rotation around its axis.

In fact, a full 360° rotation takes 23 hours, 56 minutes, and little over 4 seconds, a period known as [sidereal day](https://en.wikipedia.org/wiki/Sidereal_time). Notice that while the Earth is rotating around its axis, it’s also traveling along its orbit. In the demonstration below, which is _very_ much not to scale, you can see how after one full rotation the point on the Earth that was pointing at the Sun no longer does so and it requires some more time for that location to face the Sun again:

Out of all the stars in the sky the Sun is the one of paramount importance to our lives so the base measure of a day is the period after which the same point on Earth points at Sun again. To be more precise, we’re interested in the duration after which the Sun comes around to be directly above the same [meridian](https://en.wikipedia.org/wiki/Meridian_(geography)) – a half a circle on the surface of the Earth connecting the poles.

This also brings us to the concept of solar [noon](https://en.wikipedia.org/wiki/Noon), a time of day at which the Sun is located directly over some point at the local meridian. In the demonstration below that meridian is shown with a yellow color while the red dot shows the [subsolar point](https://en.wikipedia.org/wiki/Subsolar_point) – a location on Earth that points directly towards the Sun:

Depending on one’s position on the Earth, during a local solar noon the subsolar point is either directly north, directly south, or directly at the current location. This is also where the terms AM and PM come from. In Latin _ante meridiem_ means _before midday_, while _post meridiem_ is _after midday_.

Noon is the time of day at which the Sun is at the highest point in the sky which also means that the shadows cast by the sunlight are the shortest. Naturally, we don’t set our clocks to solar time. Instead, [time zones](https://en.wikipedia.org/wiki/Time_zone) are used to provide a more uniform timing within different regions of the world. Despite heavily [irregular shapes](https://en.wikipedia.org/wiki/Time_zone#/media/File:World_Time_Zones_Map.png) the centers of the time zones correspond to roughly noon of local solar time.

The duration between two solar noons is known as a [solar day](https://en.wikipedia.org/wiki/Solar_time) which lasts the familiar 24 hours. However, that’s not completely accurate. If you look closely at the simulation of the sidereal and solar day you’ll notice that we didn’t account for two important factors – eccentricity of the orbit and the axial tilt of the Earth. In fact, 24 hours is the duration of a _mean_ solar day. The actual duration of each individual day varies, but before we witness that variation we have to discuss the most important consequence of the axial tilt.

# Axial Tilt[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#axial-tilt)

If you were to look at the orbital plane from above you’d notice that the axial tilt of the Earth isn’t aligned to either the major or the minor axis of the orbit’s ellipse. In the simulation below you can observe the position of the Earth and its axis of rotation at different points of the year:

The four colored line segments mark four important points on that path:

- during March equinox and September equinox in the top-down view the axis of rotation is perpendicular to the direction towards the Sun
- during June solstice and December solstice in the top-down view the axis of rotation is parallel to the direction towards the Sun

Moreover, at different times of year either the Northern or the Southern Hemisphere is tilted towards the Sun which is clearly visible when we look at the orbital plane from a side with the point of September equinox pointing _directly_ at us:

The change in tilt relative to the Sun causes the familiar cycle of seasons. [June solstice](#) marks the time at which the Northern Hemisphere is maximally exposed to the Sun and the summer begins, however, at the same time the Southern Hemisphere is facing away from the Sun and in that part of the world the winter begins. The situation flips during [December solstice](#). During [equinoxes](#) both hemispheres are equally exposed, the day and night last roughly 12 hours which gives the event its name – in Latin _aequus nox_ means _equal night_.

To see the seasons in practice, let’s look at the Earth from the Sun’s perspective. The horizontal line shows the orbital plane:

Notice, that during [summer](#) on the Northern Hemisphere no matter what time of day it is the Sun never “sees” Antarctica – the Sun never rises there. Conversely, during [winter](#) on the Northern Hemisphere the Sun always sees that continent and so the Sun doesn’t set during the day.

Being directly exposed to sunlight is only a part of the seasonal picture. Despite constant exposure to Sun during summer on the Southern Hemisphere Antarctica is still a very cold place. It’s the direction at which the sunrays hit the ground that determines the amount of power the surface is exposed to.

In the demonstration below I marked three bands on the surface of the Earth – each one occupies 36° of latitude. The thin lines symbolize sunrays hitting the Earth. By changing the date you can observe how the percentage of all the rays approaching the planet is distributed among those bands:

The more perpendicular to the rays the surface is, the more energy it receives – the factor scales with a cosine of the angle between the [surface normal](https://en.wikipedia.org/wiki/Normal_(geometry)) and the direction of the incoming light. During summer months the Northern Hemisphere receives a much higher percentage of incoming rays compared to winter months which explains the average temperature difference between the two seasons.

Finally, it’s also interesting to see the sunlight from a reference frame fixed onto Earth. You can drag around to spin the globe freely in space. Yet again the red dot shows a location of the subsolar point:

What may be a little surprising is that at a _fixed_ time of day the point on Earth that points directly towards the Sun is quite wobbly when the date changes – it not only moves in north-south direction, but also in east-west direction. This effect is visible more clearly on a world map with an [equirectangular projection](https://en.wikipedia.org/wiki/Equirectangular_projection):

When seen from Earth this figure 8 shape is known as [analemma](https://en.m.wikipedia.org/wiki/Analemma). In the following demonstration you can see the position of the Sun in the sky as seen at 12:00 PM12:00 UTC from the Greenwich area in London. I chose this location since its mean solar time is pretty much the same as UTC time. The vertical lines represent angle of [azimuth](https://en.m.wikipedia.org/wiki/Azimuth). The one corresponding to 180° is located directly _south_ of the observer. The horizontal lines show angles of [altitude](https://en.m.wikipedia.org/wiki/Horizontal_coordinate_system) – the angle above the horizon. In the bottom right corner you can see which part of the sky is the observer located at the black dot looking at:

The Sun may seem tiny, but its [angular diameter](https://en.wikipedia.org/wiki/Angular_diameter) is only 0.53°, while the entire analemma spans 2 × 23.437° = 46.874° in the vertical direction. The Sun isn’t always at its highest point in the sky at 12:00 PM12:00 local mean solar time, sometimes it’s a bit ahead of time and sometimes it’s late.

The difference between the actual [apparent solar time](https://en.wikipedia.org/wiki/Solar_time#Apparent_solar_time) and the “expected” [mean solar time](https://en.wikipedia.org/wiki/Solar_time#Mean_solar_time) is described by the [equation of time](https://en.wikipedia.org/wiki/Equation_of_time). The two primary causes for the drift is eccentricity of the orbit, which by Kepler’s second law causes variation in the Earth’s orbital speed, and the axial tilt which causes difference of speed of the subsolar point in “around the Earth” direction.

The small daily differences accumulate to fairly big numbers – the Sun can be late by up to 14 minutes and ahead of schedule by up to 16 minutes against its clock-expected position. However, across the entire year the duration of a day averages out to 24 hours.

We finally have a grasp of how “a day” is measured and how important the Sun is in that picture. Moreover, the position of Sun relative to the Earth also plays a critical role for defining a year.

# Year[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#year)

If you recall our discussion of the axial tilt you may have assumed that while the direction of the axial tilt isn’t aligned to either major or minor axis of the orbital ellipse it is otherwise static. However, this is not actually the case. The axis itself slowly rotates, when seen from above, in a clockwise direction. In the demonstration below you can see how the direction changes over time. A top down view of the orbit is placed in the bottom right corner:

This effect is called [axial precession](https://en.wikipedia.org/wiki/Axial_precession) and is caused by gravitational pull of the Sun and the Moon. It takes about 25,772 years for the revolution to complete. Over time the precession will cause [Polaris](https://en.wikipedia.org/wiki/Polaris) to no longer be the north star as the Earth’s axis will point at some other direction in the starry sky. In a few thousand years it will be spring instead of winter that will begin on the Northern Hemisphere around the time of perihelion.

While the effect is very slow it has an impact on time tracking on Earth. In the exaggerated simulation below you can see how the precession causes the point of March equinox to change. In the bottom right corner you can observe the arc that the axis traverses in this period:

The thick outline of the almost complete circle shows the path of Earth between two March equinoxes. This period defines a [tropical year](https://en.wikipedia.org/wiki/Tropical_year) which, because of the precession, is _shorter_ than a sidereal year – it lasts roughly 365.2422 days. Given the importance of stable recurrence of the cycle of seasons in the calendar, it’s this period that is _the_ foundation of year tracking on Earth.

The duration of a tropical year is non-integral and after 4 years of 365 days we’re almost a full day away from the actual place on the orbit at which the March equinox occurs. A solution to this problem are leap years which in the [Julian calendar](https://en.wikipedia.org/wiki/Julian_calendar) occurred every four years.

Notice that this is a little too much of a correction – simply observing a leap year every four years makes a year last 365.25 days on average. Over the centuries the date undershoot was measurable in days and to resolve the situation the [Gregorian calendar](https://en.wikipedia.org/wiki/Gregorian_calendar) was introduced in 1582 which, other than skipping over 10 days, added some extra caveats to the simple four-year rule.

Years divisible by 100 are _not_ leap years, _unless_ they’re also divisible by 400 – the year 2000 was a leap year, but the year 2100 won’t be. This causes a year in the Gregorian calendar to on average last 365.2425 days which is a much closer match to the duration of a tropical year.

# Everything’s Moving[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#everythings-moving)

The discussion of axial precession was a hint that many of the parameters of the Earth’s motion that may seem static are in fact anything but — everything about the positioning of the Earth changes as well:

- The angle of the axial tilt varies between 22.1° and 24.5°
- The eccentricity of the orbit varies between almost 0.0 and 0.0679 with multiple overlapping cycles of different periods
- The elliptical orbit itself also rotates – an effect known as [apsidal precession](https://en.wikipedia.org/wiki/Apsidal_precession)

All those [cycles](https://en.wikipedia.org/wiki/Milankovitch_cycles) have different periods, but they all contribute to the very complex nature of the journey of the Earth through the universe.

# Further Watching and Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#further-watching-and-reading)

As usual a lot of great educational videos can be found on YouTube. Vsauce’s [How Earth Moves](https://www.youtube.com/watch?v=IJhgZBn-LHg) covers many of the same topics I’ve discussed in a more entertaining way. [Earth’s motion around the Sun, not as simple as I thought](https://www.youtube.com/watch?v=82p-DYgGFjI) by Aryan Navabi has good visuals and goes into more details of a long term cyclical nature of Earth’s motions.

For a beautiful explanation of why planets have elliptical orbits I recommend 3Blue1Brown’s [Feynman’s Lost Lecture](https://youtu.be/xdIjYBtnvZU). The video is based on a wonderful [book](https://www.amazon.com/Feynmans-Lost-Lecture-David-Goodstein-ebook/dp/B002WQLN6U) by the same title.

Nick Strobel’s [Astronomy Notes](https://www.astronomynotes.com/) provide a good overview of many topics that I haven’t covered in a form of lecture notes. [The Solar Analemma](http://www.astrosurf.com/luxorion/analemma.htm) by Anthony Ayiomamitis is a five page story about difficulties of capturing analemma on a camera.

In a traditional book form [Celestial Calculations](https://mitpress.mit.edu/books/celestial-calculations) by J. L. Lawrence is a great introduction to planetary motions. The book successfully bridges the gap between pop-science overviews of the space and the math-heavy advanced reads.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/earth-and-sun/#final-words)

I find it captivating that two seemingly separate concepts of a day and a year, driven by two different motions of Earth, are ultimately connected by the Sun and the interaction of its light with our planet.

Compared to the [modern definition](https://en.wikipedia.org/wiki/SI_base_unit#Definitions) of a [second](https://en.wikipedia.org/wiki/Second) describing the flow of time in terms of the position of the Sun in the sky may seem archaic, but up until the middle of 20^th century a second was simply defined as 1/86400 of a mean solar day.

We’ve since let go of that dependence, but the present day measure is just a much finer and _significantly_ more stable expression of pretty much the same duration. One day we’ll colonize other planets, those planets will have different suns, orbits, and rotation periods, yet a simple second will forever be tied to Earth and Sun.
