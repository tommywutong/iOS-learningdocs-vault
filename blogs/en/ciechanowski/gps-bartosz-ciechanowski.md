---
title: GPS – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/gps/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:78ac3e107a454dca'
translated: false
---

> 原文：[GPS – Bartosz Ciechanowski](https://ciechanow.ski/gps/)　·　Bartosz Ciechanowski

# [GPS](https://ciechanow.ski/gps/)

Global Positioning System is, without a doubt, one of the most useful inventions of the late 20^th century. It made it significantly easier for ships, airplanes, cars, and hikers to figure out where they are with high degree of accuracy.

One of the most exciting aspects of this system are the satellites surrounding Earth. Here’s a current constellation of active satellites, you can drag the view around to see it from different angles:

However, the satellites are just a part of what makes GPS possible. While I’ll discuss their motion in depth, over the course of this blog post I’ll also explain _how_ the satellites help a GPS receiver determine where it is, and I’ll dive into the clever methods the system uses to make sure the signals sent all the way from space are reliably decoded on Earth.

We’ll start by creating a positioning system that can tell us where we are. Our initial approach will be quite simple, but we’ll step-by-step improve upon it to build an understanding of the positioning method used by GPS.

# Simple Positioning[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#simple-positioning)

Here’s a small chunk of a world we’ll be playing with. The little **yellow figurine** represents our position in that world – you can grab and move it around. You can also drag the landscape itself to change the viewing angle. The view on the right represents a map of that landscape – we’ll try to evaluate where _exactly_ the **figurine** is on this map:

This situation may seem a bit daunting, but notice that the landscape we’re in has **three** **little** **landmarks** on the ground that are easy to reference on the map. Just by using these three reference points we can attempt to relate the **figurine’s** position in the environment to an approximate placement on the map.

Intuitively, if we’re standing right on top of one of the colored landmarks, then we can tell _exactly_ where we are on the map. If we take a single step away from a landmark, then our accuracy will degrade a little, but we’re still reasonably sure of our position. However, as we keep going further away the uncertainty in our estimate increases.

We can draw that estimation of our position on the map using a **yellow area**. Its size symbolizes uncertainty – the more of a guesswork we’re doing the bigger the circle. We also know where, more or less, to place that **yellow area** based on our position relative to the landmarks. For instance, if we’re between the **green landmark** and the **blue landmark** then we’ll be somewhere between those two dots on the map as well:

The further away from a landmark we are, the larger the uncertainty, but the _distance_ to a landmark itself also carries some information. If we attach a **rope** to a **landmark** and walk away holding the other end, it will at some point prevent us from going further. Moreover, if we keep the **rope** taut it will limit our motion to a circular path around that **landmark**:

Since the **rope** has a fixed length, every point on that circle is at the same distance to the **landmark**. Instead of using a **rope** we can attach a measuring tape to a landmark and track the measured distance as we roam around. A measured distance lets us draw an appropriately sized circle on the map, based on the map’s scale. We know that we have to be somewhere on that circle, because all the points on that circle are equally distant to the **landmark**:

If we also keep track of the distance to the **second landmark** we know that our position is somewhere on the intersection of those two circles because the intersections are the only places that have the expected distances to _both_ locations:

With two distance measurements there are only two possible positions on the map where we could be located. Measuring distance to the **third landmark** narrows down that location to just a single choice:

Notice that this third measurement is often redundant. We usually just “know” which of the two positions on the map makes sense given our position on the ground relative to the landmarks we see. In the demonstration below we’re measuring distances to just two landmarks, unless we’re almost inline with them, it’s usually fairly clear which answer is the right one:

The process of calculating a location of a point using measurement of distances is called _trilateration_ – that procedure lies at the heart of a GPS receiver. However, being tied to two or three measuring tapes is certainly _not_ how any GPS device functions, so let’s keep on making our primitive positioning system better.

# Time of Flight[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#time-of-flight)

The only purpose of the measuring tapes was to measure distances, but there are other ways to figure out how far away something is. For example, when we drive a car at a more or less _constant_ speed of 60 mph60 km/h we can easily calculate that after 15 minutes we’ve traveled a distance of around 15 mi15 km. As a side note, I’m using imperialmetric units here, but you can [switch](#) to the metricthe imperial system if you prefer.

Instead of driving from point to point we can fly a little drone around. In the simulation below you can control the progress of **time** with the slider. The clock marks the time between the drone starting and ending its journey with a **blue arc**:

In the bottom part of the demonstration I put a timeline that also tracks the duration of flight using a bit more compact representation – you can think of it as a clock unwrapped from an arc shape to a straight line. Notice that the length of the blue bar is directly tied to the duration of the flight, which in turn is directly tied to the traveled distance. When you [change position](#), the duration of flight needed to reach the goal changes as well.

The constant velocity of a drone allows us to use _time_ as a measure of distance, because that distance **s** is proportional to the _time of flight_ **t** with drone’s velocity **v** acting as a scaling factor:

s = v × t

Let’s see how we can employ two drones to replicate the measurements we did with two tapes. In the demonstration below we’re sending two drones at the same time, the slider once again controls the **time**:

As the drones arrive to their destinations we get the direct measure of distance to each landmark as shown by the length of their bars on the timeline. This allows us to draw the circles of range on the map which in turn pinpoints our position.

This method is less restrictive than the measuring tapes we’ve used, but having to fly drones to the landmarks to measure distances is still a bit ridiculous. However, the idea of using time of flight is very promising, we just need to come up with a faster and more convenient messenger.

Thankfully, we don’t have to look too far. We can use the very same substance that allows drones to fly – the _air_ itself. Instead of rapidly moving it around to generate lift for the little machines, we’ll just make noises and let the air propagate _sounds_ through itself.

# Do you hear me?[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#do-you-hear-me)

While at close ranges the sound seems to propagate almost instantaneously, at longer distances we can certainly witness the limits of the speed of sound – you’ve probably experienced the delay between _seeing_ a lightning bolt and _hearing_ its thunder. There is even a convenient rule of thumb that states that the strike was another 1 mile1 kilometer away for every 53 seconds of delay.

We can use sound to measure distances with a very simple setup. We’ll put a microphone and a light bulb at each landmark – when a microphone detects a loud sound the light bulb will turn on. To measure the distance to a landmark we’ll make a noise – I’m visualizing the propagation of that noise with a **dark ring**. As **time** passes the **sound wave** travels further and we can mark how long it took for the lightbulb to turn on:

For now we can safely ignore the delay caused by the speed of light – at our limited scale it won’t affect the measurement too much. If we mount microphones and lightbulbs at the other landmarks we can get a reliable system to measure distances, which lets us draw the circles on the map and mark our location:

This solution actually works well, but it has a fatal flaw. As soon as someone else tries to estimate their position we may have a hard time recognizing if the flash happened because of our or _someone else’s_ sound. Let’s see what happens when a **red figurine** also tries to estimate its position:

Notice that we have no idea if we should stop the clock on the first or the second flash of a landmark, but regardless of the approach our measurements may be completely wrong. Even when we use the robust method of intersecting three circles we very often fail to converge to a single location. The more users trying to estimate their positions the more error prone everyone’s range estimation would be, especially since they all can start making their noises at different times.

The problem with this approach is that we’ve created an _active_ system in which the landmarks have to actively respond to users’ requests to provide the needed information. As the number of users increases, the complexity of the system grows significantly. Even if we came up with some clever way for the landmarks to distinguish the incoming signals and emit different responses, we’re guaranteed to find some number of users that would overwhelm the infrastructure.

Fortunately, we can solve this problem by flipping it on its head. Instead of the users sending audio signals to the landmarks, we’ll have the landmarks emit the sounds and have the users listen to those sounds.

# Do I hear you?[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#do-i-hear-you)

Let’s rejig the landmarks to have a speaker that will emit a sound at every minute _on the minute_, that is when the second hand on the clock shows 0 seconds. When we hear the signal we can then check our clock to see how much time has elapsed and thus measure the distance:

It may seem that this solution works well, but it requires a bit more attention. Notice that we’re actually dealing with _two_ different clocks here, one in our hand, and another one, located in the landmark itself, that drives the sound emission. Those two clocks may not be perfectly synchronized with each other.

In the demonstration below you can see the current time as tracked by the landmark on the **system clock**, and as tracked by us on **our clock** which can be _biased_ by some amount – it could be early or late. Thankfully, with two clocks side by side we can try to correct for that **bias** using the second slider:

Notice that the timeline at the bottom shows progress of both the **system clock** and the **user clock** – if the clocks are not synchronized they’re not tracking the same time.

Unfortunately, when we’re out in the open exploring the environment we don’t necessarily have access to the **system clock** so we don’t know _how_ to synchronize **our clock** with the **system clock**. Even if we initially synchronize our clocks, they may drift apart over time. Our measurement of absolute time may be biased relative to the “true” **system time**.

This has dire consequences – a landmark always emits its signal on the minute on the **system clock**, but we think the signal was emitted on the minute on **our clock**. Our estimate of the actual start time may be incorrect. Depending on the **bias** of **our clock**, this can cause us to under or overestimate the time of flight:

For the sake of clarity I’m still drawing the **blue bar** on the timeline, but remember that we actually don’t know what the current **system time** is. The system always emits the signal when the **blue bar** is at 0 seconds, but _we_ think that the system emitted its signal when the **red bar** is at 0 seconds.

If we get lucky and **our clock** [is synchronized](#) with the **system** then what we consider the sound emission time will match exactly the _actual_ emission time. If our clock is [running behind](#), then when we think the signal has [just been emitted](#) it has actually been flying through the air for a while. Conversely, if our clock is [running ahead](#), then when the signal is [actually emitted](#) we erroneously assume it’s already been in the air for a while.

Because of that unknown **time bias** we’re no longer calculating the _true_ time of flight and therefore we’re not measuring the _true_ range. Instead, we calculate a so-called _pseudorange_. The length of a pseudorange depends on what we assume the bias to be. This distance uncertainty sounds like trouble, so let’s see how the presence of **bias** affects our ability to draw circles on a map:

Notice that the circles on the map now change their radius with our attempts to account for the unknown **bias**. We can no longer rely on just two circles as their intersection points move around with different values of that unknown **bias**.

We’re seemingly in big trouble, but there is an additional assumption we can make – we can safely expect the clocks in the landmarks to be synchronized with each other. Their location is stationary which means they can use large and very precise clocks that are continuously monitored to ensure synchronization. Since all the clocks in the landmarks have the same **system time**, this also means that the **bias** of **our clock** to each of the landmarks is _exactly_ the same.

Because that **bias** is the same, all three of the measured distances are either too short, or too long by _the same_ amount, and that amount depends precisely on the **bias** of **our clock** relative to the **system clock**. Here’s where the third measurement becomes indispensable:

After we get [all three signals](#) and we try to guess what the actual value of **bias** was, there is only [one value](#) of **bias** at which all three circles intersect in one place – that’s where we are on the map.

This is a monumental achievement. We’re not only calculating the correct position, but also the exact value of the **bias** of **our clock**, so this setup also allows us to synchronize **our clock** with the **time of the positioning system** – we get a reliable source of accurate time. The only additional cost we had to pay for all of this is the need for the third emitter at a known location.

Moreover, the infrastructure we’ve built is completely agnostic to the number of users it services. The emitted sounds don’t care how many receivers are listening, each one can perceive the sounds on their own without interfering with anyone else’s measurements:

# Leveling Up[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#leveling-up)

So far our movements were restricted to just a flat 2D plane, but interesting things happen when we allow the **figurine** to get above the ground level. In the demonstration below you can control the user’s **vertical position** with a slider. To make things simpler, let’s go back to our original idea of using measuring tapes to evaluate the distances:

Notice that as the figurine gets [above the ground level](#), the distances to the landmarks increase. We can no longer use the method of circles on the map, as they don’t even converge on the same location.

When we allow movement in three dimensions, our transformations of distances to plain circles are no longer valid. Instead, a fixed distance defines an entire _sphere_ around the marked point. For easier visualization let’s first just put all three markers floating freely in a 3D space. A known **distance** to the first location puts us somewhere on the surface of that sphere:

With a **second measurement** we can narrow down the possible location to the circle created by an intersection of two spheres:

To account for the third measurement we need to add a _third_ intersecting sphere – it lets us narrow down the position to **two possible points** where three circles intersect:

While we technically need a fourth sphere to differentiate between those **two points**, three ranges are usually enough to figure out the exact position – if the centers of the spheres are far enough apart, one of the two possible solutions would be underground or in space.

Let’s see how those concepts fit onto our map. To visualize the spheres we can no longer keep its surface lying flat. To make things easier to reference, I made the map rotate in sync with the main view. Notice that the intersection point of the three spheres lets us pinpoint the position _and_ altitude even as you drag the **figurine** around:

Throughout these examples we’ve been using the simple system of measuring tapes, so let’s try to go back to the solution that used sound waves and pseudoranges. Recall that it didn’t require the user to have the clocks perfectly synchronized:

Notice that the new dimension added a new complication. While in a flat case we could have just look for a single value of **bias** for which the three circles have intersected, there are a lot of _different_ values of **bias** for which the three _spheres_ intersect and we’re incapable of precisely determining both the position and the altitude at which we are.

By analogy to the flat case, we need to add a _fourth_ landmark to resolve this problem. We can then look for the value of the unknown **bias** that makes four spheres intersect at a single location:

This method of measuring pseudoranges to at least four emitters at known positions is _exactly_ what GPS uses to calculate the receiver’s position and the time bias of its clock.

Before we continue developing our simple system, it may be worth pausing for a second to show the math underpinning the hand-wavy sphere resizing we’ve been doing so far. We’re dealing with four distances to four emitters and we end up with four equations:

(x − x~1)^2 + (y − y~1)^2 + (z − z~1)^2 = v × (t~1 − b)

(x − x~2)^2 + (y − y~2)^2 + (z − z~2)^2 = v × (t~2 − b)

(x − x~3)^2 + (y − y~3)^2 + (z − z~3)^2 = v × (t~3 − b)

(x − x~4)^2 + (y − y~4)^2 + (z − z~4)^2 = v × (t~4 − b)

The left sides of the equations are just distances between the **unknown position** of the receiver and each of the **red**, **green**, **blue**, and **yellow** emitters, calculated with 3D Pythagorean theorem. On the right side we have the four times of flight **t** from the emitters to the receiver, the unknown receiver bias **b**, and velocity of propagation **v** which so far has been the speed of sound.

We’re ultimately trying to solve this system of equations to get the receiver’s **x****y****z** position and its bias **b**, but for the rest of the article I’ll keep using the more abstract description of the problem since the mathematical operations aren’t critical for our understanding of GPS.

# Higher, Better, Faster, Stronger[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#higher-better-faster-stronger)

It seems that the infrastructure we’ve built allows us to correctly calculate our position and clock correction when we’re close enough to the landmarks. If we want to make our positioning system work on the entire planet like GPS does we still have a few problems to solve.

Firstly, sound waves aren’t the best way to send the signals around. Periodic loud beeping would be annoying to everyone around, but, more importantly, sounds get dispersed in the air quite quickly – you can’t easily hear things that make sounds tens of mileskilometers away.

A good candidate for a better carrier would be light. Similarly to sound, it also has a limited speed of propagation which we can use to measure the traveled distance. The speed of light in vacuum **c** is absolutely enormous and it has the following exact value that, per its definition, I’m showing in metric unitsvalue:

c = 299 792 458 m/s

It only takes light one billionth of a second to travel the distance of around 1 foot30 cm. Unfortunately, light gets easily obscured by some atmospheric effects like fog, dust, clouds, or smoke so instead of visible light we’ll use another form of [electromagnetic radiation](https://en.wikipedia.org/wiki/Electromagnetic_radiation) – a radio wave of a certain frequency.

The second problem preventing us from deploying this system globally is related to visibility of the signal emitters. So far we assumed that our local environment is perfectly flat, but when a radio wave encounters a hill it gets blocked, which you can experience in the following simulation. In many cases the receiver will never get the signal unless we put the emitter high enough using the second slider:

By putting the emitter [at an altitude](#) we can thankfully mitigate that problem on a local scale. Unfortunately, we’ve also been ignoring another important obstacle – the curvature of the Earth itself. To see that curvature, however, we have to rise way above the ground and venture into the blackness of space.

In the demonstration below you can witness how the emitted waves are masked by the shape of the planet depending on the altitude of the **emitter**:

The Earth’s curvature acts as a hill that obscures areas that lie beyond the horizon as seen by the **emitter**. Thankfully, the higher we put the **emitter**, the larger the area it sees. We can visualize that area in three dimensions using a cone:

Naturally, we can’t build an arbitrarily tall tower, so to put an **emitter** well above the ground level we’ll have to attach it to a _satellite_ that we’ll place high enough that it sees a reasonably big section of Earth. One could naively hope that we can just put a satellite in any place in space and it will just stay there, but unfortunately things aren’t that simple.

# Orbits[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#orbits)

Let’s see what would happen to an object if we could magically put it motionless in space somewhere around the Earth. In the demonstration below you can drag the **yellow object** around. Once you let it go it will get pulled by the Earth’s gravity which I’ve symbolized with **little blue arrows**. As the **object** starts to move a **yellow arrow** reflects its current velocity:

Note that the strength at which the **object** is pulled towards the planet varies with distance. That force of gravity **F** pulling an object is proportional to the mass of that object **m** and mass of the Earth **M**, but it’s _inversely_ proportional to the square of the distance **r** between the centers of their masses:

F =  G × m × M / r^2

The constant **G** is known as the [_gravitational constant_](https://en.wikipedia.org/wiki/Gravitational_constant) and it’s very small – it takes an object of an enormous mass like that of the Earth for the force of gravity to be perceptible at our human scales.

Regardless of where in space we put a _motionless_ object, it will eventually fall down on Earth, but interesting things happen when the object’s initial velocity is _not_ zero. In the demonstration below you can once again drag the **object** around, but this time it will have some initial velocity that was perhaps given to it by a rocket. Once you let go, the **object** will initially move in that direction, but the Earth’s **gravity** will still keep pulling on it:

Notice that the movement of the **object** is much more interesting now – the **gravity** keeps redirecting the **object** towards the center, but it manages to stay ahead of that pull which results in an elliptical trajectory. Notice that the speed of the **object**, as shown by the length of the **yellow arrow**, varies over the course of its journey. When the object is far away from Earth the gravitational field is weak and it takes a while for **gravity** to change the **object’s** direction of travel, but close to Earth the strong gravitation quickly accelerates it.

If the trajectory [intersects Earth](#), the object will still fall down on ground, but in [other cases](#) it will instead _orbit_ Earth on an elliptical path. You may have also [managed](#) to make the trajectory **red** – the object is on a [_hyperbolic trajectory_](https://en.wikipedia.org/wiki/Hyperbolic_trajectory) and it will just fly away and never come back.

Naturally, we want the radio signal emitters to stay in the vicinity of the Earth so for our purposes only elliptical orbits are useful. I’ve [discussed ellipses](https://ciechanow.ski/earth-and-sun/#ellipse) on this blog before, but it’s worth doing a quick recap.

Before we continue, I need to note that some demonstrations in the following sections are animated – you can play and pause them by clickingtapping on the button in their bottom left corner. By default all animations are enabled, but if you find them distracting, or if you want to save power, you can [globally pause](#) all the following demonstrations.disabled, but if you’d prefer to have things moving as you read you can [globally unpause](#) them and have animations running.

The easiest way to draw an ellipse is to take two **small pins** and wrap a string around them. If we then put a **yellow pencil** inside that loop and keep the string taut while moving the **pencil** around we’ll draw an ellipse. By moving the **pins** closer or further apart we can change the generated shape:

Notice that I’m painting sections of the strings with different colors. As we go around the curve, **red** and **blue** parts trade lengths, but the _sum_ of their lengths is always the same which is the defining property of an ellipse. The **small pins** are the _focal points_ of that ellipse.

The shape of an ellipse is determined by its [_eccentricity_](https://en.wikipedia.org/wiki/Eccentricity_(mathematics)). In this string contraption eccentricity is the ratio of the length of the **green** section to the sum of lengths of **red** and **blue** sections. The size of an ellipse is defined by its [_semi-major axis_](https://en.wikipedia.org/wiki/Semi-major_and_semi-minor_axes) which is half of its widest point, or half of sum of lengths of **red** and **blue** parts. When [eccentricity is 0](#), an ellipse becomes a circle and it’s semi-major axis is just the circle’s radius.

Length of the semi-major axis of a satellite’s elliptical orbit is one of its most important parameters. We’ve already seen how the area of the Earth seen by a satellite changes with the distance. More importantly, as discovered by Kepler and formalized in his [third law](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion#Third_law), the length of the semi-major axis **a** is tied to the time **T** it takes a celestial body to complete a single orbit – the quantity known as [_orbital period_](https://en.wikipedia.org/wiki/Orbital_period):

a^3 = T^2 ×  G × M / 4 × π^2

As a result, the further away the satellite is, the longer it takes to trace a full ellipse which you can experience in the demonstration below. Notice that the ellipse is embedded in a plane known as _orbital plane_, I’ve visualized it with a **yellow disc**:

For example, the International Space Station is [very close](#) to Earth and it orbits the planet in just under 93 minutes – roughly 15.5 times per day. Notice that there is only [one orbit](#) that takes 23 h 56 min 4 s – the length of a [sidereal day](https://ciechanow.ski/earth-and-sun/#sidereal_day_paragraph) during which the Earth performs a single revolution around its axis. Satellites with that orbital period are called _geosynchronous_. Let’s look at them up close. The **red dot** shows a point on Earth where a geosynchronous satellite is directly above the observer:

Notice that after a single revolution of the Earth the satellite returns to the same position. You may have noticed that the **red slider** controls the _inclination_ of the orbit which is the angle between the **orbital plane** and the **plane** passing through the Earth’s equator known as _equatorial plane_. When that angle [measures 0°](#) the red point doesn’t move on the Earth at all, the satellite is always present at the same point in the sky, and that orbit is known as a _geostationary_ orbit.

A geostationary orbit sounds like a good choice for placing a bunch of satellites of a positioning system, as each one would have a fixed and known position in the sky and a receiver could just measure distances to the ones it sees. However, that approach has a few problems.

In the demonstration below, you can control the number of geostationary satellites that are evenly distributed across the orbit. Each satellite is visible to a different section of the planet, but as the number of satellites grows, some areas of the Earth see more and more satellites. The number of visible satellites from that location on Earth is represented using colors of increasing **intensity**:

With 10 satellites [in place](#) all parts of the Earth close to equator have visibility of at least 4 satellites required to calculate the position and time offset. Unfortunately, even with a huge number of geostationary satellites the areas close to the South and North Pole would never see any satellites making the system not completely global.

Another problem with geostationary satellites is related to any configuration where all satellites lie on the same plane. Let’s look at one of those configurations in which the satellites are closer to Earth making things easier to see. In the demonstration below you can drag the **red point** around to change its position on the globe. The **darker red lines** show calculated distances to each of the visible satellites:

Notice that on the other hemisphere there is a **white point** that, due to symmetry, has the _exact_ same distances to the satellites! If positioning satellites were arranged on the geostationary orbit we wouldn’t be able to tell if we’re on southern or northern latitudes using trilateration as the only cue because we can’t determine which of the two possible options is the right one.

With those restrictions in mind, we can now discuss how the Global Positioning System solves these problems by using satellites that do _not_ use geostationary orbits and as such do _not_ have a fixed position in the sky for the observers on Earth.

# GPS Orbits[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#gps-orbits)

Let’s look at an orbit of a single GPS satellite around the Earth. The **red point** shows a location on Earth where the satellite is directly above an observer:

A single GPS orbit has an inclination of around 55 degrees and an orbital period of 11h 58m 2s which is a half of a sidereal day causing them to pass over the same place on Earth twice per day. This was particularly useful during GPS development when only a limited number of satellites was available, but their periodical visibility in the sky could’ve been consistently relied on.

GPS consists of 6 different orbits placed around the Earth. Originally, each orbit contained 4 satellites for a total of 24 satellites. However, these days there are 30 active GPS satellites which improves accuracy and ensures redundancy. In the demonstration below you can select each of the 6 orbits or show all satellites from the entire _constellation_:

Notice that within an orbit the satellites aren’t evenly distributed. As Earth rotates and satellites move around the number of satellites visible from a point on Earth changes. In the demonstration below you can drag the **red point** on Earth to observe the satellites it sees:

We can also visualize the number of visible satellites from _every_ point on Earth. Let’s look at that coverage of by marking different regions of Earth with colors of different **intensity** – it once again represents the number of visible satellites:

While I’m not accounting for local hills or buildings, you can observe that each part of the Earth is easily covered by at least 4 satellites allowing the receiver to calculate its position and clock bias. We’ll soon see that the more satellites visible, the better accuracy of the predicted position is, but not all placements of satellites are equally favorable.

With all those satellites moving in the sky you may wonder how a receiver can know where the satellites are. The solution to this problem is simple yet absolutely brilliant – each satellite _tells_ the receiver where it is as a part of its broadcasted signal.

# Keplerian Elements[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#keplerian-elements)

There are many ways to specify a position in space, but traditionally six [Keplerian elements](https://en.wikipedia.org/wiki/Orbital_elements#Keplerian_elements) are commonly used. The first two elements, **semi-major axis** and **eccentricity**, specify the size and proportions of the orbital ellipse. For satellites, Earth is one of the focal points of the ellipse:

GPS satellites have a **semi-major axis** of around 16503 mi26560 km and **eccentricity** of around 0.02 or smaller.

The next two elements, **inclination** and **longitude of the ascending node**, specify the orientation of the orbital plane relative to Earth and distant stars:

We’ve already seen **inclination** in action – GPS satellites operate at an inclination of around 55°. **Longitude of the ascending node** deserves a bit more explanation. Notice that the ellipse of satellite’s orbit intersects the **equatorial plane** at two different locations known as _orbital nodes_ – I’ve marked them with **red** and **green** dots. The **green** one is the _ascending node_, because the satellite rises up or _ascends_ at that location – it moves north.

**Longitude of the ascending node** is the angle on the **equatorial plane** measured from a [certain reference direction](https://en.wikipedia.org/wiki/First_Point_of_Aries) that is fixed against distant stars and doesn’t follow the Earth’s rotation. GPS constellation consists of 6 different orbits – their **longitudes of the ascending nodes** are evenly separated by 60°.

The last two elements, **argument of perigee** and **true anomaly**, specify the position of the orbital ellipse and the satellite itself:

**Argument of perigee** defines the orientation of the ellipse within the orbital plane measured from the ascending node to the **perigee** that is the point on the ellipse closest to Earth – I marked it with a **yellow dot**. The final parameter is **true anomaly**, which is the angle between the **perigee** and the satellite itself as measured _at a specific time_.

In an idealized scenario, that fixed set of six parameters would be enough to calculate the current and _future_ positions of a satellite at any point in time, but unfortunately there are other effects at play. A satellite’s orbit gets perturbed from pristine Keplerian pathways by other effects like the not perfectly spherical shape of the Earth, the gravity of Moon and Sun, and solar radiation. As part of the broadcasted message GPS satellites also include information of the _rate_ of change of some of those parameters, which allows the receivers to calculate necessary corrections over time.

You may wonder how a GPS satellite knows all of these parameters. All GPS satellites are being tracked by monitoring stations on Earth. Those stations are part of the _Control Segment_ of Global Positioning System which manages the satellites and the contents of messages they broadcast. Every two hours, updated orbital parameters and clock adjustments are uploaded to satellites, which ensures that the information sent from satellites to the receivers is as accurate as possible.

Knowing the position of a satellite on its orbit one can convert from Keplerian elements to **x****y****z** coordinates in a Cartesian system tied to Earth. The details aren’t important here, but the calculations account for a lot of different factors including the rotation of the Earth within the short time between the signal emission and the signal reception. As we’ve seen before, the process of figuring out the location also requires accurate tracking of time, but that concept deserves a bit more elaboration.

# Time[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#time)

Trilateration with time of flight as a measure of distance requires that the clocks on all emitters are synchronized, and that is indeed the case for GPS. Each satellite carries a precise atomic clock and additionally the control stations can apply corrections to individual satellites to keep them in sync. That unified time is known as _GPS time_ which for technical reasons is offset from the “standard” [UTC time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) by an integer number of seconds.

When it comes to the _flow_ of time on those satellites, there are two important aspects related to Einstein’s theories of relativity. [Special relativity](https://en.wikipedia.org/wiki/Special_relativity) states that a fast moving object experiences time dilation – its clocks slow down relative to a stationary observer. The lower the altitude the faster the satellite’s velocity and the bigger the time slowdown due to this effect. On the flip side, [general relativity](https://en.wikipedia.org/wiki/General_relativity) states that clocks run faster in lower gravitational field, so the higher the altitude, the bigger the speedup is.

Those effects are not even and depending on altitude one or the other dominates. In the demonstration below you can witness how the altitude of a satellite affects the dilation of time relative to Earth. The progress of time is tracked by two separate bars. When the **yellow bar** gets filled it means that one second has elapsed on the **satellite**. When the **blue bar** gets filled it signifies that one second has elapsed on **Earth**. Notice that at high altitudes a second on the **satellite** finishes faster than a second on **Earth**, but at very low altitudes a second on the **satellite** takes longer to finish. Since the actual dilation is minuscule, the difference of bar lengths is greatly magnified to make things easier to see:

Satellites at the [GPS altitude](#) travel at the speed of about 2.4 mi/s3.87 km/s relative to Earth, which slows the clock down, but they’re also in weaker gravity which causes the clock to run faster. The latter effect is stronger which in total results in a gain of around 4.4647 × 10^−10 seconds per second, or around 38 microseconds a day.

Unfortunately, this is where many sources make a mistake with their interpretation of that result. It’s often erroneously claimed that if GPS didn’t correct for these relativistic effects by slowing down the clocks on satellites, the system would increase its error by around 7.2 mi11.6 km per day as this is the distance that light travels in those 38 microseconds.

Those assertions are not true. If relativistic effects weren’t accounted for and we let the clocks on satellites drift, the _pseudoranges_ would indeed increase by that amount every day. However, as we’ve seen, an incorrect clock offset doesn’t prevent us from calculating the correct _position_. The calculated receiver clock bias would also be correct, but that bias would be relative to the drifting satellite clock making it much less useful.

Moreover, the clocks on satellites don’t have to be explicitly slowed down to fix the cumulative relativistic speed-up of time. As part of their broadcasted message a satellite emits three coefficients that allow the receiver to correct for any offset or speed change of that satellite’s clock.

One area where we _explicitly_ have to account for relativistic effects is caused by slightly eccentric trajectories of the GPS satellites. As a satellite orbits the Earth its distance and speed relative to the planet change, which then causes periodic variations in the satellites’ clock speeds. Since the receiver knows the satellites’ positions it accounts for that relativistic variation when calculating timing corrections.

Unfortunately, this is not the only source of complications for evaluation of the time of flight.

# Signal Propagation[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#signal-propagation)

While for most of their journey GPS signals travel uninterrupted through the vacuum of space, at some point they encounter the Earth’s atmosphere which affects them with two different mechanisms. In the upper part of the atmosphere known as the [_ionosphere_](https://en.wikipedia.org/wiki/Ionosphere), the solar radiation ionizes gasses, which increases the number of free electrons that slow down propagation of the coded message. The amount of free electrons and the slowdown depend on time of day and overall solar activity.

In the lowest part of the atmosphere, mostly in the [_troposphere_](https://en.wikipedia.org/wiki/Troposphere), the larger density of gasses and water vapor increases the [index of refraction](https://ciechanow.ski/cameras-and-lenses/#lens_wave_glass), which also slows down the radio signals. The water vapor amount can be highly variable, making the delay in signal’s time of flight unpredictable.

The strength of these _ionospheric_ and _tropospheric_ delays also depends on the length of the path that radio signals have to travel in the **atmosphere**, which in turn depends on the **elevation angle** of the **satellite signal** relative to the receiver. We can see this in this [backlit view](https://en.wikipedia.org/wiki/File:Thin_Line_of_Earth%27s_Atmosphere_and_the_Setting_Sun.jpg) of the Earth:

As that **angle** increases, the **signal from a satellite** travels more sideways and its larger portion gets **affected** by the **atmosphere**. To account for this, GPS receivers ignore ranges measured from satellites at very low elevation angles.

While atmospheric effects are primary source of GPS inaccuracies, other sources of disturbances also exist. For example, the clocks on all satellites can’t be _perfectly_ synchronized. The orbital elements and their rates are also measured with some degree of uncertainty, so both the positions and timestamps received from satellites are not exact. On Earth the signal can bounce off different surfaces and take a longer path to reach the receiver compared to direct reception.

Although many of these factors can be to some extent accounted for, the measured distances to satellites will have some degree of error – we no longer deal with a single distance but a certain allowed _range_ of distances. What this means is that the spheres we’ve been intersecting actually have some thickness and we’ll never be able to get a perfect solution where a few spheres of ranges intersect at a single spot.

We can try to visualize this thickness with actual satellites but you’ll probably agree that’s it’s quite hard to see what’s going around on the draggable **red point** even though I’m trying to reduce the clutter by only drawing halves of the spheres:

To make things easier to see let’s briefly drop down to a two dimensional case and consider a simplified scenario with signals from just three satellites. In the demonstration below, you can control two parameters: the **uncertainty** of the measured distance, which ends up corresponding to the thickness of the border of the circle of range, and the **relative position** of these satellites.

The receiver’s position is somewhere in the **intersection** of these three regions – the smaller that region the better the accuracy of our position estimation. Naturally, large **range uncertainty** [increases](#) the ambiguity of position, but the relative position of the satellites also matters. If they [aren’t well spread](#), the exactness of calculated location also suffers. In this example we’ve also assumed that the **uncertainty** of measurement is the same for all satellites, but it usually won’t be the case.

To account for all these issues GPS receivers try to find such a set of four solutions, three position coordinates and the clock bias, that will in some sense be a best fit that minimizes the error – this is where using data from more than 4 satellites allows a receiver to improve the accuracy.

The calculated clock bias may seem like a trivial companion to the much desired location, but it’s very useful in many applications that require time synchronization – we literally get easy, albeit indirect, access to atomic clocks.

Since we’re talking about a receiver on Earth, it’s only appropriate if we come back from the darkness of space to the bright surface of our planet.

So far I’ve been fairly vague about the message that reaches a receiver, what that message contains, and how it’s decoded, but those details are fascinating – I’ll discuss them in the last two sections of this article.

# Navigation Message[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#navigation-message)

The information sent by a GPS satellite is collectively known as a _navigation message_. I’ll go over most of its pieces one by one, but first let’s look at its structure. The entire message consists of 25 **frames**, each **frame** consists of 5 **subframes**. Each **subframe**, represented by a single row, consists of 10 **words**, and each **word** consists of 30 bits:

|  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|
|  | TLM | HOW | Clock corrections, health |  |  |  |  |  |  |  |
| TLM | HOW | Ephemeris |  |  |  |  |  |  |  |  |
| TLM | HOW | Ephemeris |  |  |  |  |  |  |  |  |
| TLM | HOW | Almanac/other – page 1 |  |  |  |  |  |  |  |  |
| TLM | HOW | Almanac – page 1 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  | TLM | HOW | Clock corrections, health |  |  |  |  |  |  |  |
| TLM | HOW | Ephemeris |  |  |  |  |  |  |  |  |
| TLM | HOW | Ephemeris |  |  |  |  |  |  |  |  |
| TLM | HOW | Almanac/other – page 2 |  |  |  |  |  |  |  |  |
| TLM | HOW | Almanac – page 2 |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
| ··· |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |
|  | TLM | HOW | Clock corrections, health |  |  |  |  |  |  |  |
| TLM | HOW | Ephemeris |  |  |  |  |  |  |  |  |
| TLM | HOW | Ephemeris |  |  |  |  |  |  |  |  |
| TLM | HOW | Almanac/other – page 25 |  |  |  |  |  |  |  |  |
| TLM | HOW | Almanac – page 25 |  |  |  |  |  |  |  |  |

The first two **words** of every **subframe** have the same structure. **TLM**, or telemetry word, contains a fixed preamble that’s easy to recognize, and some bits intended to check the integrity of the message. **HOW**, or handover word, is vital for GPS functionality – it timestamps the **subframe**, which lets the receiver figure out when it was emitted.

The subsequent 8 **words** of each **subframe** carry different payload. The first **subframe** contains the satellite clock corrections and the week number of GPS time, which, together with the more fine-grained timestamp from handover word lets the receiver calculate the exact time the message was sent.

This **subframe** also contains a “health” bit, which describes if the navigation data is in a good state. When an orbit of a GPS satellite needs to be adjusted, the Control Segment will temporarily toggle that bit to let the receivers know that they shouldn’t rely on the information from that satellite as it tweaks its position.

The next two **subframes** contain the already mentioned orbital parameters extended by velocity information which are collectively known as _ephemeris_ parameters – they allow the receiver to calculate the satellite’s position.

The first three **subframes** are always present in every **frame** and they contain data related to this satellite, but the last two **subframes** contain the coarse ephemeris data for _all_ satellites – that collection is known as _almanac_. This lets the receiver approximate when a new satellite would rise above the horizon. The other information carried in these **subframes** include health of other satellites and some parameters that allow the receiver to try to account for ionospheric delay.

As you can imagine, this entire payload is fairly large, so it is split across 25 pages – a single **frame** contains only a single page placed in the last two **subframes**. The receiver has to gather all 25 **frames** to fully decode that supplementary information.

The data rate at which GPS satellites send their signals is astonishingly small – they transfer only 50 bits every second. At that rate sending just the text contents of this article would take almost 2.5 hours. This means that a single **subframe** consisting of 10 **words**, each occupying 30 bits, takes 6 seconds to transfer and a single **frame** is received over 30 seconds.

That 6 second granularity of timestamps in each **subframe** is very coarse, but, as we’ll soon see, the way the bits of the navigation message are encoded and decoded carries with it a lot of additional precision.

# GPS Signals[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#gps-signals)

While at a high level the navigation message can be divided into **frames**, **subframes**, and **words**, it ultimately consists of individual bits of **data**, each equal to either 0 or 1. A GPS satellite emits these bits over time which we can represent on an animated plot. In the demonstration below, when the bit of the **source data** has a value of 1 the plot jumps above the horizontal axis, but for 0 it simply stays on it:

The data payload is transferred over radio waves in a [specific range](https://en.wikipedia.org/wiki/L_band) of the radio spectrum that is not obscured by atmospheric effects and can reach the receivers on Earth regardless of the outdoor conditions. While modern GPS satellites emit signals at a few different frequencies, the primary civilian signal is broadcasted at 1575.42 MHz by all satellites. I will represent that **base radio wave** with the following sine wave:

On its own, a steady radio wave like that doesn’t convey much information, but we will use it as a _carrier_ wave that we’ll modulate to make it carry the payload of data. There are many ways to do that modulation. We could, for example, multiply the **carrier wave** by the stream of **data bits** effectively turning the **emitted signal** on and off:

For transmission of its signals, GPS uses a _different_ method known as [_binary phase-shift keying_](https://en.wikipedia.org/wiki/Phase-shift_keying#Binary_phase-shift_keying_(BPSK)). Conceptually, the binary signal of ones and zeros gets adjusted to replace every 0 with −1, and then that **signal** gets multiplied by the **carrier wave**:

That multiplication by −1 ends up shifting the signal’s [phase](https://en.wikipedia.org/wiki/Phase_(waves)) which explains the name of the method. If we were dealing with just a single satellite this method of encoding would be sufficient as the receiver could just remove the carrier from the **incoming signal** and decode the **data bits**:

In reality things are more complicated. There are many satellites broadcasting at the same time, so the data bits from all of them overlap. Additionally, the GPS signals reaching Earth are incredibly weak and they get swamped with noise, which would make a bare data payload indecipherable:

GPS solves this problem by employing another binary code. This **code** repeats over time and consists of a predetermined number of so-called _chips_. In this example there are 6 chips in the **code**:

The chipping code changes at a higher rate than the source bits. To encode the signal the satellite multiplies the **data bits** of the navigation message by that **code**. Let’s see how this idea works in practice:

In this example, for every bit of the **data signal**, we’re repeating two sets of the same **code**. Notice that the negative value of **data signal** ends up flipping the **coding signal** as well.

The **input data**, the **code**, and the **carrier wave** are all multiplied together to create the **final signal** that the satellite emits:

I need to note that for the sake of clarity I’m using a visually compact example – each bit of the **navigation message** is represented by 2 lengths of the repeating **code**, each **code** consists of 6 chips, and each chip lasts 2 wavelengths.

In real GPS signals those numbers are much larger. There are 20 repetitions of the chipping code inside a single bit of the message and each chipping code consists of 1023 individual chips. Each chip then lasts for 1540 wave cycles. If we multiply all these numbers together we get 31,508,400 wave cycles per bit, which, at 50 bits per second, ends up as the exact 1575.42 MHz.

Moreover, we’re actually dealing with an entire family of these codes – every satellite has a unique one. In the demonstration below you can see the first three of the so-called PRN codes that the GPS satellites emit:

Even though the codes look like a binary random noise, they’re in fact _pseudorandom_ which explains their name – PRN stands for pseudorandom noise. Each of those codes is well known and can be easily recreated.

The addition of the code may seem like a needless complication, but it’s actually extremely useful. Those pseudorandom codes have two important properties. The first one defines how well a code correlates with its copy shifted in time. Let’s see what this means in practice on a much shorter code of length 63. In the demonstration below you can slide a **replica of the code** and see the signal it generates when multiplied by the repeated **original code**:

The bottom section of the simulation shows the sum of the **positive** and **negative** areas of the product of the **code** and its **replica** as well as the **difference** of these two areas. Notice that when the [replica is not aligned](#) the **difference** of areas is relatively small, but when we [manage to align](#) the replica with the signal the **difference** shoots up greatly. The correlation of the code signal with a copy of itself, or _auto-correlation_, is very high only when things are aligned correctly, and that jump in the magnitude of **difference** lets us detect that alignment.

The second important property is related to _cross-correlation_, or correlation with coding signal from a _different_ satellite. Let’s see what happens when we slide a **replica of code from satellite 1** against a **code from satellite 2**:

As you can see, when we slide the **replica** around the **difference of areas** comes up a little bit, but it never reaches the highly discernible peak we’ve seen for auto-correlation.

Those two properties unlock the magic that happens in the receiver. Let’s take a look at a simplified version of those steps, at first using a **clean incoming signal** from just a single satellite. The receiver can remove the sinusoidal carrier wave and get the **signal** that is a product of the navigation message and the chipping code:

The receiver can then create the **replica** of the chipping code for a satellite it’s trying to track, and then check if it can find a high correlation peak between the **input signal** and that **replica** as measured in the highlighted region. The receiver tweaks the offset until it finds high **difference of areas** which lets it know it found the correct offset value:

As you observe the **difference of areas**, that is **positive area** minus **negative area**, after the [correct offset](#) is found, you may notice that over time it flips between being positive and negative. Since the coding signal was originally multiplied by the sign-flipping data signal, the flipping we see on the plot is actually the decoded data – you can compare the plot of the **difference of summed areas** to the original **data signal** that I’m showing at the bottom for completeness. After the correct offset has been found, the receiver can just look at the sign of that **difference** to decode the data bits.

The time offset of the **replica** provides the receiver with additional timing information that lets it calculate the exact elapsed time of flight. Recall that each subframe of a GPS message is timestamped with a granularity of 6 seconds, which, on its own, would be atrociously low precision.

However, by keeping track of how many bits we’ve seen, how many code repeats we’ve seen, and the chip offset into the code we can significantly improve that precision. The receiver knows how much time each of these components occupies so it can add that duration on top of the timestamp encoded at the beginning of the subframe. We’re effectively timestamping each chip or even its fractions. When the receiver is measuring the time of flight, this method lets it calculate that duration very precisely.

Finally, let’s see how the cross-correlating properties allow the receiver to distinguish between different satellites. In the demonstration below, the **input signal** is a combination of the signals emitted by a few visible satellites as well as some noise. You can select which of the replicas the receiver is generating and adjust the offset to tune in to a satellite’s signal:

After some tuning we can find the required time offsets to decode signals from [satellite 1](#), [satellite 2](#), and [satellite 3](#), but we can’t find a good match for satellite 4. This is a likely scenario as only some of all the 30 satellites are visible at once to a receiver.

I need to emphasize that this was a simplified analysis of signal processing intended to illustrate how the chipping code allows the receiver to recover the original data bits. The behavior of an actual receiver is more complicated than what I’ve described. One of those additional complexities worth mentioning is the velocity of a satellite relative to the observer on Earth. Due to [Doppler effect](https://en.wikipedia.org/wiki/Doppler_effect) this changes the frequency of the signal as seen by the receiver. To correctly acquire the signal the device has to tune in on both the time offset _and_ the appropriate frequency.

Finally, it’s worth reiterating that the receiver doesn’t need to send anything to the satellites, it just listens to the signals that the satellites restlessly emit without knowing if anyone receives them.

# Further Watching and Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#further-watching-and-reading)

[GPS MOOC](https://scpnt.stanford.edu/about/gps-mooc-massive-open-online-course) was an online course hosted by Stanford in 2014. Thankfully, the video recordings of the lectures are [available on YouTube](https://www.youtube.com/watch?v=o1Fyn_h6LKU&list=PLGvhNIiu1ubyEOJga50LJMzVXtbUq6CPo) and I highly recommend them for a deeper dive into GPS workings. Both presenters are experts in their domains and do an excellent job explaining the topics.

The textbook [Global Positioning System](https://www.gpstextbook.com) by Pratap Misra and Per Enge provides an even more detailed exposition of the discussed topics. It’s a thorough, but very readable publication on GPS and satellite navigation – it was my primary source for this article. I particularly liked that the book does a high level overview of all the elements of the system at first and then explores them individually in depth in later chapters.

For a personal description of the history of GPS I recommend [the interview](https://ethw.org/Oral-History:Brad_Parkinson#Parkinson.27s_educational_background_and_the_origins_of_GPS.5D) with [Brad Parkinson](https://en.wikipedia.org/wiki/Bradford_Parkinson), who was the lead architect of the system. While the interview was conducted in 1999, still relatively early days of consumer GPS, Brad correctly predicted an upcoming explosion in widespread personal use.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gps/#final-words)

It’s fascinating how much complexity and ingenuity is hidden behind the simple act of observing one’s location in a mapping app on a smartphone. What I find particularly remarkable is how many different technological advancements were needed for GPS to work.

Just the satellites themselves required the development of rockets, mastery of orbital controls, and manufacturing prowess to build devices capable of withstanding the extremes of space.

Precise time tracking was made possible by the invention of an atomic clock, while advancements in radio transmission and clever coding algorithms allowed the very weak signal sent by satellites to be correctly deciphered on Earth by receivers, which were in turn dependent on microchips and the digital revolution.

It’s hard not get inspired by the relentless drive of people who kept pushing science and technology forward. All of their work made GPS an indispensable tool in our everyday life.
