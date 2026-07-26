---
title: Gears – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/gears/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:cdd62c46df54667e'
translated: false
---

> 原文：[Gears – Bartosz Ciechanowski](https://ciechanow.ski/gears/)　·　Bartosz Ciechanowski

# [Gears](https://ciechanow.ski/gears/)

I’ve always been fascinated by mechanical gears. There is something captivating about the way their teeth come together to create a fluid, unified motion:

In this blog post I’d like to look at these simple machines up close. I’ll explain how gears affect the properties of rotational motion and how the shape of their teeth is way more sophisticated than it may initially seem.

Movement is important in this article so most of the visualizations are animated – you can play and pause them by clickingtapping on the button in their bottom left corner. By default the animations are enabled, but if you find them distracting, or you want to save power, you can [globally pause](#) all animations, just make sure to unpause them as needed.disabled, but if you’d prefer to have things moving as you read you can [globally unpause](#) them and see all the objects in their rotating glory.

# Spinning[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#spinning)

On a hot summer day you might have enjoyed a cool breeze from a desk fan. Let’s take a closer look at this device. In the demonstration below you can control the fan’s speed using a slider:

The speed of a rotating fan is a different kind of speed than that of a car – it describes how quickly a fan _rotates_. To distinguish that rotating movement from a simple linear motion we use the term _angular velocity_. Angular velocity describes how quickly an object rotates relative to some point. For mechanical devices like fans that point often corresponds to the center of a shaft on which the spinning part is mounted.

Angular velocity can be expressed in many units. In physics and math the most popular ones are _degrees per second_ (°/s) and _radians per second_ (rad/s) – they express the change in object’s angle of rotation per unit of time:

In engineering it’s more common to use the unit of _revolutions per minute_ or _rpm_ for short. Older spinning hard drives rotated at 5,400 rpm while an internal combustion engine of an idling car may keep running at around 800 rpm. Almost by definition, the second hand of a clock rotates at 1 rpm.

All of °/s, rad/s, and rpm are equivalent – they’re just one multiplication by a constant factor away from each other. Given the engineering nature of this article I’ll stick to rpm, but I’ll often skip the units completely since they won’t be essential.

# Disc[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#disc)

Propeller-like shapes are exciting to look at, but they obscure some basic features of the rotational motion that we’ll explore. Over the next few paragraphs we’ll look at a more basic shape – a disc attached to a shaft. In the demonstration below you can control its angular velocity with a slider:

The small triangular indicator is there to help visualize the current orientation of the disc. I’ve also painted six points on its surface. You may have already noticed that some of those points move more than the others even though the entire disc has the same angular velocity.

Let’s investigate what’s going on by controlling the time back and forth with a slider. As the disc rotates the points leave a trace of the path they followed:

At the bottom part of the simulation you can see the flattened arcs of the paths traced by the six points. Notably, as the disc rotates the distances traveled by the points further away from the center are larger than those of the points closer to the center. Coincidentally, the triangular pattern of the flattened out arcs is also a simple way to [derive](https://www.cut-the-knot.org/Curriculum/Geometry/RABH.shtml) the area of a circle.

All paths are traversed in the same amount of time, but their lengths differ signaling that the points have different _velocity_. Notice that we’re talking about a different kind of velocity now. The disc and all the points on it have the same _angular_ velocity, but different points at different radii have different _linear_ velocities.

In the demonstration below you can observe how the arrows, which represent the linear velocities of the six points, change depending on the disc’s angular velocity and the points' distances from the center:

The instantaneous linear velocity **v** of a point on a rotating object depends on the distance **r** to the center of rotation and the angular velocity **ω**:

v = ω · r

A linear velocity of a point rotating around the center of rotation is perpendicular to the direction towards the center. As a side note, observe that while the linear velocity vector constantly changes its _direction_ due to [centripetal acceleration](https://www.khanacademy.org/science/physics/centripetal-force-and-gravitation/centripetal-acceleration-tutoria/a/what-is-centripetal-acceleration), its _magnitude_ remains the same.

# Transmission[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#transmission)

So far we’ve been looking at just a single rotating disc, but let’s try to complicate things a little by adding a second disc to our setup. I’ll place it so that the side surfaces of the discs are pressing against each other. In the demonstration below the _driving_ yellow disc is powered by some engine, which I’ve indicated using a rotating arrow near the shaft. You can observe what happens to the green disc that isn’t powered by anything:

The two discs aren’t perfectly slick, their surfaces have some roughness to them which creates friction when the sides touch. That friction at the contact point between two discs is making them temporarily stick to each other. This causes the right circle to be “dragged” along for the ride. At some point the curvature of the discs pulls the connection apart, but as that happens new points on the surfaces of the discs are coming into contact again.

Observe how the two discs rotate in different directions – as one turns clockwise the other one rotates counterclockwise. Moreover, due to sticking at the point of contact the velocities of the side surfaces of both discs are the same. All the points on those sides trace the same arcs in the same period of time.

In that simple scenario as the driving disc completed a full turn, so did the driven disc. Things become more interesting when the discs have _different_ radii. Let’s look at the paths that two points on the surfaces of these discs trace:

Since the linear velocities of the points are the same, the paths end up having the same length. However, this causes the bigger disc to rotate by fewer degrees since its circumference is larger. In this configuration, when a small disc does a full turn the big one does _half_ a turn. The _angular_ velocity of the right disc is _smaller_.

We can reach the same conclusion by looking at the velocity of the “sticking” point. The linear velocity **v~in** as seen by the **in**put disc is:

v~in = ω~in · r~in

While the linear velocity **v~out** of the **out**put disc is:

v~out = ω~out · r~out

Since these velocities are the same we can simply equate them:

ω~in · r~in = ω~out · r~out

To finally derive that the angular velocity of the output disc is proportional to the angular velocity of the input disc:

ω~out = ω~in · r~in / r~out

The smaller the input disc, the smaller the output angular velocity, and the smaller the output disc, the _larger_ its angular velocity.

In the demonstration below the left driving disc always rotates with the same angular velocity, but the angular velocity of the right disc is affected by the ratio of radii of the two wheels:

The speed of the driven green disc can change quite drastically depending on the ratio of the radii. We’ve devised a very simple mechanism that allows us to modify the angular velocity from one shaft to another. However, it’s not all this contraption is doing.

# Torque[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#torque)

The next time you tighten a nut with a wrench try to see how the force needed to move it depends on the point at which you apply the force. The demonstration below shows roughly how big of a force would be needed:

The further away from the nut you press the lesser the force needed and the easier it becomes to tighten the nut. If you don’t have a wrench and a nut handy, you can try to open a door by pressing it very close to the hinge. It’s much harder to do compared to pushing the door near the handle – the capability to turn is much smaller.

This turning effect of a force is called _torque_ and it depends on both the applied force **F** and the length of the lever arm **r**:

T = r · F~t

Notice the little ~**t** subscript next to the force – it represents the _tangential_ component of the force. In the demonstration below you can control the angle of the applied **gray** force, however, only the **red** tangential component that is perpendicular to the arm ends up counting towards the torque:

Notice how the magnitude of torque increases and decreases as the force rotates. When the force starts pushing the wrench in the opposite direction the torque changes sign because it also changes the clockwiseness of the rotation of the wrench.

The alternative way to look at the tangential component is to find a circle that is tangent to the line of force and use its radius **r~t** as the basis for the torque calculation:

As such, torque can also be expressed using this form:

T = r~t · F

Both approaches to look at this problem are equivalent as they ultimately end up being described by the same equation in which **α** represents the angle between the force and the arm:

T = r · F · sin(α)

So far we’ve discussed how a force acting on a perpendicular arm creates a torque. However, if a torque is already present on a shaft, e.g. exerted by an engine or a crank, then that torque will apply a force at a distance.

In the demonstration below a disc has a spool attached to it on which a rope is wound. The disc has a constant input torque, but as the radius of the spool changes so does the force with which the rope is pulled:

When two friction discs are working together the driving one drags the driven one with some force, so let’s see how the torque is affected by the interaction between two discs. A torque **T~in** on an **in**put shaft causes the disc to exert force **F** at a distance **r~in**:

F = T~in / r~in

That very same force acts on the **out**put disc at a distance **r~out**:

F = T~out / r~out

We can equate the two:

T~in / r~in = T~out / r~out

To finally derive that the output torque is proportional to the input torque:

T~out = T~in · r~out / r~in

Let’s compare the equation for the output torque with the equation for the output angular velocity:

ω~out = ω~in · r~in / r~out

Notice that the ratios of the radii are inverted. We can now see how the torque and angular velocity are affected in an actual disc setup. In the simulation below you can control the ratio of radii of the two discs. The right disc has a spool with a rope attached to it. Since the spool is attached to the disc the torque and the angular velocity are transferred directly to it:

Notice that when the yellow _driving_ gear gets smaller the torque on the output disc increases and as a result so does the force with which the rope is pulled. On the other hand, as the _driven_ gear gets smaller its angular velocity increases and so does the linear velocity of the rope.

By using two discs of different radii we can use a single engine to drive the input and have vastly different outcomes at the output. Depending on the use case we may want to sacrifice some speed to be able to pull the rope with a lot of force, or prioritize the output velocity at the cost of a weaker pulling capability.

# Gears[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#gears)

The friction discs systems we played with so far work perfectly in idealized scenarios, but in practice they’re quite flawed. As soon as the two discs are not in a close contact due to vibration, wear on the touching surfaces, or even manufacturing imprecision, they’ll start slipping. The assumption about the sticking contact point breaks and the mechanism no longer transfers angular velocity and torque as needed:

This problem can be solved by ensuring that the driving wheel physically _pushes_ the driven wheel. This is where gears come in. Because the teeth of two _meshed_ gears are interlocked with each other, the driving gear ends up pressing directly against the driven gear:

Let’s look at an example of two gears of different sizes meshing with each other. Naturally, for two gears to be compatible their teeth have to be of the same size – the distance between two subsequent teeth known as _circular pitch_ has to be the same. In the demonstration below each gear has its circular pitches marked with short arc segments. Notice down below that those arcs flattened out have the same length:

A full circular set of colorful segments forms a so-called _pitch circle_. A pitch circle represents an idealized circle that is in contact with the other gear’s pitch circle. They both correspond to the simple friction-based disc systems we’ve already discussed.

Pitch circles let us look past the complexity of the interlocking gears by reducing their form to the familiar teethless discs on which we can used the radius-based equations. However, using the size of gear’s radii or diameter is cumbersome, especially since the pitch circle isn’t visible.

In practice, it’s more common to refer to gears by using their number of teeth **N** and the size of those teeth. In the United States the term _diametral pitch_ is used to define the teeth size, it is obtained by dividing the number of teeth **N** by the diameter **d** of the pitch circle.

diametral pitch = N / d

In other countries a similar, but inverted ratio called _module_ is used instead:

module = d / N

Both diametral pitch and module effectively define the _size_ of the teeth. Since those parameters in the two matching gears have to be the same we can equate them:

N~in / d~in = N~out / d~out

With just a simple transformation we can derive that the ratio of the number of teeth is equivalent to the ratio of the diameters, or the radii, of the pitch circles:

N~in / N~out = d~in / d~out  = r~in / r~out

As a result we can talk about a transmission system using number of teeth on the meshing gears instead of specifying their diameters or radii:

T~out = T~in · N~out / N~in

ω~out = ω~in · N~in / N~out

In the demonstration below you can adjust the _diametral pitch_, i.e. the size of the teeth of the two meshed gears to see that the constant ratio of the numbers of teeth indeed maintains the constant ratio of angular velocity:

# Tangent & Normal[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#tangent--normal)

So far I’ve conveniently avoided describing the details of the shape of the teeth of a gear, but it’s actually one of the most important aspects of a gear system. Before we take a closer look at the profile of a tooth we have to discuss the concept of a _tangent_ to a curve.

A [tangent](https://en.wikipedia.org/wiki/Tangent) can be described in a few different ways, but one of the most intuitive ones is to imagine three beads sliding on said curve. The red bead symbolizes a point on the curve at which we want to find the tangency. The two blue beads neighbor the red bead at its sides:

As the blue beads get closer and closer to the red bead, the line spanned through their centers approaches the line of tangency at that red point. The tangent line shows the local “straight ahead” direction on the curve. In the limit, the imaginary beads completely overlap and the tangent locally touches the curve at just a _single_ point which explains the origin of the word – in Latin _tangere_ means “to touch”.

A closely related concept to a tangent line is a _normal_ line which is perpendicular to the tangent at that point. In the demonstration below you can see the dotted normal and the solid tangent lines of two curves:

When two curves [touch](#) at a single point, their lines of tangency, and thus normals, are the same. If it wasn’t the case then a line of tangency of one curve would intersect the other curve in more than one place and the shapes would be overlapping instead of meeting at just a singular location.

This observation is important when we consider the point of contact between two teeth. Let’s see it up close:

The **black** point represents a _pitch point_ – a point at which the two pitch circles of the gears touch. The **red** point represents the point of contact between two teeth – notice how it moves across the surfaces of the teeth. The solid line shows the tangent line of the outline of two teeth at the point of contact and the normal is represented by the dotted line.

The only useful component of the contact force between the two gears will be acting in the direction of that normal – that’s the pushing force which I depicted using the black arrow. You may wonder if the fact that the direction of the force in the previous demonstration is tilted matters. After all, it may affect the transfer of torque.

Let’s look at this problem in a little more detail. Since transmission features of gears are ultimately decided by their pitch circles we can simplify the situation by analyzing the effective pitch circles of the teeth-less discs when the force changes direction:

When we discussed torque we already observed that when the force changes direction the radius of the circle tangent to that force also changes. However, the radii of _both_ discs are scaled by the same factor of **cos(α)**, where **α** is the _pressure angle_ controlled by the slider in the simulation above:

T~out = T~in · r~out·cos(α) / r~in·cos(α)

In effect, the cosine factors cancel out and the constant ratio of torque transfer is maintained. In the example above the line of force always passed through the black pitch point in the center. In the simulation below you can witness what happens to the effective circle radii when the line of force does _not_ go through the pitch point:

As you can see, if the acting force doesn’t lie on the line through the pitch point one of the circles effectively grows while the other one effectively shrinks. The constant torque ratio is _not_ maintained since the ratio of the effective radii also changes.

A very similar line of thinking can be done for the rate of change of angular velocity. A point of contact between two gears has some linear velocity related to the rotational motion of the discs. Since the two teeth remain in contact, the components of the velocities in the direction of the normal have to be the same, otherwise the teeth would separate.

From here the reasoning is equivalent to our analysis of forces – if you’re interested you can follow a [more rigorous derivation](https://eng-resources.uncc.edu/unccengkit/mechanical/gears/law-of-gearing/) that I found. The final conclusions for both angular velocity and torque are the same and our discussion of the surface normals helps us define the _law of gearing_:

> To ensure a constant ratio of angular velocity and torque modification the surface normals of teeth at all points of contact have to go through the pitch point.

As long as that condition is met, the tooth profiles can be arbitrary. However, in practice a very specific curve is used to define the shape of a gear’s teeth. Let’s see how it’s created.

# Strings Attached[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#strings-attached)

The tooth shape we’re looking for should ensure that its normal at any point of meshing will point at the pitch point. We could let the normal change direction over time, but to make things simpler we can just define a single line on which all normals will lie. We could look at this setup through equations, but thankfully a much more pleasant approach exists.

We’ll take two discs, wrap a string around them, and we’ll nail that string to the discs' sides so that it follows their movement. Let’s see what happens when we put a little perpendicular **red** marker on that string and start unwinding it from one disc and winding it onto another. I attached a piece of paper to the underside of the yellow disc so that we can see the trail left by the marker as the disc rotates:

The straight part of the string represents the normal – that’s the direction in which the pushing force will act. For the force to act in this way the tangent of the curve should be _perpendicular_ to the string at all times. However, that’s exactly what the red marker does – at every point of the curve it is perpendicular to the string, and thus it’s perpendicular to the normal. The trail left on the paper is precisely the curve we were looking for.

We can look at this same situation from a point of view of the single disc, by unwinding a string with a marker from its surface:

The shape we’ve created is called an _involute_. At every point of the curve its normal is tangent to the generating circle precisely because the taut string _is_ that normal. If the teeth of two matching gears have an [involute](https://en.wikipedia.org/wiki/Involute) profile they meet the requirements of the law of gearing.

A shape of involute of the teeth in a gear is generated by the gear’s _base circle_, which is _smaller_ than its pitch circle. The smaller size of the base circle results in a non-zero pressure angle, the most commonly used value is 20°. As we’ve seen this is perfectly fine since due to the shape of the involute the force is directed through the pitch point.

In the demonstration below you can see how a shape of teeth of an _idealized_ gear is formed:

The shape starts at the [dedendum circle](#) which defines the bottom outline of the teeth roots. From here the teeth grow radially in **blue** straight lines – these areas of the teeth are never in contact with the teeth of the other gear.

Once the [base circle](#) is reached, the **red** involute shape begins – from every side an imaginary string is being unwound. The magic marker at the end of the string passes through the [pitch circle](#), which corresponds to the idealized friction disc, only to end at the [addendum circle](#) which defines the outline of the teeth tips.

In practice, the bottom part of the tooth would join the dedendum circle with a [fillet](https://en.wikipedia.org/wiki/Fillet_(mechanics)) to avoid stress concentration and its shape would be heavily influenced by the way a gear is manufactured. The widths of the teeth would also be slightly narrower to allow some [backlash](https://en.wikipedia.org/wiki/Backlash_(engineering)) to prevent jamming.

What’s interesting about involute gears is that even for the same size of teeth, as measured by diametral pitch or module, the shape of a tooth of a given gear strongly depends on the gear’s radius. In the simulation below the **green** line shows the pitch circle, the **red** line shows the base circle of the involute, and the slider controls the radius of the gear:

Two matching involute gears with different number of teeth, and thus different radii, will have slightly _different_ shapes of teeth. In the limit, when the radius of a gear is infinite, the involute becomes a straight line. A segment of a gear with infinite radius is called a [rack](https://en.wikipedia.org/wiki/Rack_and_pinion). That linear gear is commonly found in a steering mechanism of a car.

The involute has another practical property – it maintains the constant transmission ratio even when pitch circles of the two gears aren’t in perfect positions. This allows for some inaccuracies in the placement of the two shafts driving the gears.

Thanks to many useful properties the involute is the most commonly used tooth profile, however, some applications make use of non-involute gears. For example, [cycloidal](https://www.tec-science.com/mechanical-power-transmission/cycloidal-gear/meshing-of-cycloidal-gears/) gears are used in clocks and watches.

# Multiple Gears[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#multiple-gears)

Let’s see what happens when we add a third gear to the system:

Firstly, notice that introduction of the third gear has reversed the direction of the output shaft – it now rotates in the same direction as the first. Let’s calculate how the second blue gear has affected the angular velocity of the third green gear. We can express the final angular velocity of the third gear as:

ω~3 = ω~2 · N~2 / N~3

We also know that the angular velocity of the second gear depends on the first one:

ω~2 = ω~1 · N~1 / N~2

The substitution yields:

ω~3 = ω~1 · N~2 / N~3  · N~1 / N~2  = ω~1 · N~1 / N~3

When three gears are connected like that the number of teeth of the middle, so-called _idler_ gear, doesn’t matter for the angular velocity and torque of the output.

We can create a multi gear system in another way. In the demonstration below the red and blue gears are fixed together and they both rotate with their shaft at the same angular velocity:

Let’s peek at the equations of the pairs of meshing gears. The fourth green gear is driven by the third red gear:

ω~4 = ω~3 · N~3 / N~4

And the second blue gear is driven by the first yellow gear:

ω~2 = ω~1 · N~1 / N~2

In this case, however, angular velocities of the third and second gear are the same:

ω~3 = ω~2

And we end up with:

ω~4 = ω~1 · N~1 / N~2  · N~3 / N~4

Similar logic applies for equations of torque transfer:

T~4 = T~1 · N~2 / N~1  · N~4 / N~3

In this configuration all four gears participate in the final ratio of adjustment. A multi stage transmission enables a significant reduction in size of the assembly – a single stage setup with 4:1 reduction like in the example above would have to be both wider _and_ much taller. Additionally, with multiple stages a machine can change the gearing ratios relatively easily like it happens in a [manual transmission gearbox](https://www.youtube.com/watch?v=wCu9W9xNwtI).

Even if you never plan to design a functional set of gears, it may be worth knowing how _not_ to design one. In the demonstration below you can see what happens when the three gears are meshing with each other – the mechanism gets jammed:

By moving the blue gear slightly to the left we can see that the yellow gear wants to rotate it clockwise, however, by placing the blue gear to the right we can see that the green gear wants to rotate it counterclockwise.

Unfortunately the “three jammed gears” pitfall is [quite common](https://www.lockhaven.edu/~dsimanek/whoops.htm#gears) in graphic design. However, if you try really hard and have access to a 3D printer, you may actually be able to pull off at least [_some_ version](https://www.youtube.com/watch?v=5Mf0JpTI_gg) of it.

# Further Watching and Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#further-watching-and-reading)

[This Old Tony](https://www.youtube.com/channel/UC5NO8MgTQKHAWXp6z8Xl7yQ) is an amazing YouTube channel devoted to machining and metal working. Tony’s video on [gears and gear cutting](https://www.youtube.com/watch?v=qVN2jrn4Kuo) is informative _and_ entertaining at the same time. His quirky sense of humor certainly adds a great value to the thorough explanations.

For joyful torture tests of LEGO parts I highly recommend [Brick Experiment Channel](https://www.youtube.com/channel/UClsFdM0HzTdF1JYoraQ0aUw). The video collection showcases capabilities of plastic LEGO gears to increase [angular velocity](https://www.youtube.com/watch?v=s3BsDF6UjCQ) or [torque](https://www.youtube.com/watch?v=pvE83NfbZ8g) to ridiculous levels – the author managed to coerce a basic battery-powered LEGO motor to lift 100 kg of weight.

In this blog post I’ve only talked about the simple _spur_ gears. As usual, you can read about some other [kinds of gears](https://en.wikipedia.org/wiki/Gear#Types) on Wikipedia. The entire [article](https://en.wikipedia.org/wiki/Gear) is quite thorough and includes this [wonderful image](https://en.wikipedia.org/wiki/Gear#/media/File:Interactive_gears_in_the_hind_legs_of_Issus_coleoptratus_from_Cambridge_gears-3.jpg) of natural gears found in [some planthoppers](https://en.wikipedia.org/wiki/Issus_coleoptratus).

Finally, [tec-science](https://www.tec-science.com/category/mechanical-power-transmission/) is a great resource on various engineering concepts. The series on [mechanical power transmission](https://www.tec-science.com/category/mechanical-power-transmission/) dives deeper into the topics I’ve discussed here. I particularly like that the site’s articles often include high quality [3D renders](https://www.tec-science.com/mechanical-power-transmission/gear-types/cylindrical-gears/).

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/gears/#final-words)

The considerations behind real world gears are much more complicated than what I’ve presented. The physical world is messy – the gears aren’t perfectly rigid, they thermally expand during operation, and their surfaces wear over time. All of these factors have to be accounted for in the domain of engineering.

Despite all that, under the murky waters of physical reality, the idealized mathematical principles of gears are still there. I’ve hopefully shown you that gears aren’t just some discs with teeth – there is a lot of mathematical ingenuity in their design.
