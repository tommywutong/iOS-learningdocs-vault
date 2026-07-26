---
title: Curves and Surfaces – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/curves-and-surfaces/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4675ae5d83d65be2'
translated: false
---

> 原文：[Curves and Surfaces – Bartosz Ciechanowski](https://ciechanow.ski/curves-and-surfaces/)　·　Bartosz Ciechanowski

# [Curves and Surfaces](https://ciechanow.ski/curves-and-surfaces/)

From fonts to animated movies, curves and surfaces constitute fundamental building blocks of many geometrical designs. Over the course of this blog post I’ll explain how this model of a mask can be very smooth despite being described by a limited number of small points  that you can drag around to change the mask’s shape:

Moreover, we’ll see how surfaces like that are a natural extension of plain two dimensional curves like the one below:

Throughout this article I’ll keep jumping back and forth between curves and surfaces to highlight how the ideas we develop for wiggly lines can be expanded onto three dimensional shells that we can shape.

# Defining the Shape[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#defining-the-shape)

Before we build complicated curves and surfaces we first have to decide how we’d like to control their shape. There are many ways to describe and mold these objects, but some of those ways are better than others. In the demonstration below I built a system that lets you change the shape of a **curve** by controlling its **spiral‑ness** and **size**:

While fun to play with, this system is quite impractical. We can’t control where exactly the curve ends and we also have a very limited influence on _how_ it twists. For instance, it’s impossible to create an S‑shaped curve using these controls.

Ideally, we’d deal with a system that would let us directly affect where the curve is placed, while also providing a convenient control over its entire shape. These are the features that _control points_ provide. Their visual placement makes it very easy to define the shape of a curve. In the demonstration below you can drag each control point shown as  to change the **curve’s** form:

Control points are often visualized with connecting lines that join them to their neighbors. This helps to avoid ambiguities when two different points [swap their positions](#) which can make the curve look quite different.

Notice that all control points seem to affect the shape of the curve in the point’s vicinity. We can visualize the impact of a given point using red color. In the demonstration below you can tapclick a control point to see how it affects the local shape – the **redder** the section of the curve the more influenced it is by that control point. **Gray** sections don’t move at all when the selected point is dragged:

With control points we can easily change where the curve starts, ends, and how it flows in the middle. Moreover, the shape of the lines connecting the control points roughly resembles the shape of the resulting curve. This system of control points is simple, yet very powerful.

So far I’ve been quite vague about the rules driving the shape of the resulting curve and the extent to which the control points affect it. I’ll try to explain those underlying principles by building this system from a ground up. We’ll also see how those ideas extend to surfaces, but before we construct these more complex elements we’ll start with the simplest curve – a linear segment.

# Linear Segment[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#linear-segment)

In the demonstration below you can drag the control points **A** and **B** around to change their position. The slider controls a virtual **red pen** that is used to draw a segment between those two points:

While this demo is the world’s most primitive drawing application, there are some important observations we can make here already. The **slider** controls the _progress_ of our drawing – the more advanced the slider is the further into drawing we are. For the [progress of 0.5](#) we’re halfway through a drawing, and at the [progress of 0.9](#) we’re mostly done.

Additionally, a point on the segment [very close](#) to point **B**, as shown by the tip of the pen, moves very little when point **A** is dragged, but it moves a lot when point **B** is dragged.

We can visualize the “weight” of a given control point on the curve using the red tinting we’ve seen before. You can tapclick the control points to change which one is selected:

For a linear segment like that, weighting function is quite straightforward. The closer to the control point we are the more impactful it is. Let’s try to put some numbers behind these dependencies.

There are many ways to specify the impact of a control point at a distance, but the simplest approach is to assume that those weights are changing proportionally with that distance. As we **progress** through the curve using the slider we decrease the weight of the point **A** and increase the weight of the point **B**:

This hopefully makes intuitive sense. When we’re [all the way](#) through the curve the weight of the point **A** is 0 and we can move it around all we want without affecting the position of the end of the curve.

We can describe those little plots using some equations. A word **“progress”** would make the formulas very long so I’ll replace it with the traditionally used letter **t**:

t = progress

The position of any point **P** on the linear segment for given progress **t** is:

P = A × (1 − t) + B × t

We’ll see those **(1 − t)** and **t** terms a lot, so to make them easier to distinguish I’ll **mark them** and I’ll put little triangles on their right sides to quickly visualize if that section goes up or down with the progress – those triangles match the shapes of the plots we’ve just seen:

P = A ×

+ B ×

This equation describes [_linear interpolation_](https://en.wikipedia.org/wiki/Linear_interpolation) and it will be very important in our further discussions. We can indeed verify that e.g. plugging progress **t** equal to 1 simply returns the point **B**.

It may not be immediately clear what it means to multiply a point by a number so let’s explore that a little. Ultimately, each point has **x** and **y** coordinates that define its position relative to some origin:

When we multiply a point by some number we’re actually individually multiplying its **x** and **y** coordinates:

P~x

=

A~x

×

+

B~x

×

P~y

=

A~y

×

+

B~y

×

We can see that process in a visual form by tracking the coordinates of all three points as the **progress** changes:

P~x

=

A~x

×

(1.00 −

t

)

+

B~x

×

t

=

P~y

=

A~y

×

(1.00 −

t

)

+

B~y

×

t

=

The entire **linear segment** itself is ultimately created by infinitely many points constructed from all possible values of **t** between 0 and 1.

# A Step Further[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#a-step-further)

So far we’ve been dealing with flat 2D segments, but nothing prevents us from doing the same operations in a three dimensional space. In the demonstration below you can control the position of points **A** and **B** in a 3D space by dragging them around. You can also change the viewing angle by dragging anywhere else. The **slider** controls a virtual pen that paints a **linear segment**:

By dragging that point through space we’ve created a simple linear segment placed in three dimensions. However, now we can go a step further by dragging that segment through space to create a **red surface**:

The surface we’ve just made is fairly arbitrary and not very well defined, but the concept is very promising, so let’s try to create a simple surface that we can easily control. The idea is simple – we can place two linear segments in space that will form **rails** on which another **dragged segment** slides:

Notice that in [many configurations](#) the **dragged segment** will change its length as it goes, but that is actually beneficial – it lets us create more varied shapes.

It’s important to note that we move along the side segments proportionally – when we’re [halfway through dragging](#) we’re also halfway through the lengths of the **rails**, even if the **rails** themselves have [different lengths](#). You can think of the **blue rails** as a sort of interconnected sliders.

Let’s not forget that the segment we’re dragging is itself made by dragging a point between the segment’s endpoints, so the entire surface consists of points made from all possible values of _two_ different progresses, one **along the rails** and another **along the dragged segment**:

The sliders, and thus the progresses, are independent of each other, so we can think of the choice they offer as a 1×1 square:

One slider controls the progress **t** of the dragged segment and the other slider controls the progress **s** _within_ that segment.

That arrangement of sliders is a bit cumbersome, so I’ll just keep both of them in a horizontal orientation. I’ll occasionally put a smaller version of this square in the bottom left corner of a demonstration – it will make it easier to analyze how the sliders control the placement of a **point** on the surface:

It may also be useful to see how different arrangements of the control points deform that input square in the 3D space. As you deform the surface the lines remain straight, but the distances between them may change:

Let’s try to express what we’ve built so far in a mathematical manner. Let me show the initial demonstration with different points labeled to makes things easier to reference:

The end points **P~0** and **P~1** of the **dragged segment** are just interpolated end points of the **rails** **AC** and **BD**:

P~0 = A ×

+ C ×

P~1 = B ×

+ D ×

Then the position of the point within the segment is just another linear interpolation:

P = P~0 ×

+ P~1 ×

After plugging the values we can indeed confirm that the final position of a point **P** on this surface depends on _two_ parameters **s** and **t**:

P

=

(

A

×

+

C

×

)

×

+

(

B

×

+

D

×

)

×

Which we can expand to see the functions driving each point:

P

=

A

×

×

+

B

×

×

+

C

×

×

+

D

×

×

The terms next to the control points may seem a little complicated, but in fact they’re fairly simple once represented visually. They are the 2D equivalents of the 1D weighting functions we’ve already seen. I’m once again using **redness** _and_ height to visualize how impactful that control point is on different areas of the surface:

Notice that the weighting functions are symmetrical to each other. As a result, we can create the very same surface by choosing to drag either the **yellow** _or_ the **blue** segment through space – they both end up tracing the same surface:

While we’re effectively just dragging a straight stick through the air, the surface it creates, known as a [_hyperbolic paraboloid_](https://en.wikipedia.org/wiki/Paraboloid#Hyperbolic_paraboloid), at some viewing angles [doesn’t look straight](#) at all – there are some curvy shapes to be found on this surface.

In general case any point sliding on the surface traces some sort of curve through space. However, a particularly interesting curve appears when a point moves across the diagonal of the input square region – we can easily show the **trajectory** of that **point** by locking the two sliders together:

Notice that while the **point** always follows the same straight linear path on the input square, for [many configurations](#) the **path traced** on the surface forms a _non_‑straight **curve**. Let’s try to write the equation of that **curve**. To recap, any point on the surface we’ve looked at can be described using the following equations:

P

=

A

×

×

+

B

×

×

+

C

×

×

+

D

×

×

However, because the sliders are locked together, **s** and **t** are the same so we obtain:

P

=

A

×

×

+

B

×

×

+

C

×

×

+

D

×

×

Notice that both B and C points have the same weights so we can tie them together:

P

=

A

×

×

+

(B + C)

×

×

+

D

×

×

We can simplify things even further if we make points **B** and **C** overlap each other. Observe that this makes the entire surface flat and the curve gets nicely isolated:

Since points **B** and **C** are the same, this gives us the final simplified form:

P

=

1

×

A

×

×

+

2

×

B

×

×

+

1

×

D

×

×

Note that we’re dealing with just three points so from now on I’ll call the third point **C** instead of **D**. The curve we’ve built is known as a _quadratic [Bézier curve](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)_. Here it is being drawn in just two dimensions:

I think it’s very gratifying that we’ve found this smooth curve hiding on the surface obtained by dragging a _straight_ segment through space.

Let’s look at how much each point affects the shape of the curve as we **advance** through it. You can tapclick a control point to select it:

There are a few interesting observations to be made here:

- When the **progress** is [equal to 0](#) the weight function of control point **A** reaches 1 and all the other disappear, so the curve is guaranteed to start at point **A**
- Similarly, when the **progress** is [equal to 1](#) the weight function of control point **C** reaches 1 and all the other disappear, so the curve is guaranteed to _end_ at point **C**
- When **progress** is [between](#) those two extrema the position of the points on the curve is affected by all 3 control points

It’s also worth pointing out that the “speed” of travel along the curve is no longer constant like it was for a linear segment. We can visualize how uniform steps of **progress** map to the curve points:

For [some configurations](#) when the slider is [halfway](#) along the progress, the curve is definitely _not_ halfway drawn. In some applications, e.g. when an object is expected to move along a curve with constant velocity, that discrepancy between the “input” progress and actual progress of distance along the curve may be very important, but for our visual use cases it won’t matter.

Quadratic Bézier curves are unfortunately fairly limited. For instance, it’s impossible to express any sort of loop with a plain curve like that. To get better control over the shape of the curve we need to somehow introduce additional control points that would give us finer tunability of the curve’s form.

Looking at the equations and weighting functions it may be a bit hard to figure out how we could generalize the curve to introduce more points. Let’s look the at that equation again:

P

=

1

×

A

×

×

+

2

×

B

×

×

+

1

×

C

×

×

We can split the doubled **B** part and rearrange things a little to get:

P

=

(

A

×

+

B

×

)

×

+

(

B

×

+

C

×

)

×

It may seem that we only made things worse, but in fact we simplified things greatly. Notice that the values in the parentheses are just linear interpolations between points **A** and **B** as well as **B** and **C**. We can call these new points **AB** and **BC**:

AB

=

A

×

+

B

×

BC

=

B

×

+

C

×

And then the final point **P** is just a linear interpolation of the two:

P

=

AB

×

+

BC

×

Let’s look at what we’ve derived using some visuals:

We essentially interpolate points on the edges that we have, to create a new edge on which we then interpolate again to get the **point** on the **curve**. Now, if we introduce another control point we can just repeat this idea by doing repeated interpolations. Notice that at every step we have one fewer point and one fewer edge:

This curve is known as a _cubic_ Bézier curve. If we tally up all the interpolations we do we end up with the following compact form:

P

=

1

×

A

×

×

×

+

3

×

B

×

×

×

+

3

×

C

×

×

×

+

1

×

D

×

×

×

Observe how **(1 − t)** sections convert to **t** sections for the subsequent points. All those multiplications of triangular functions end up creating the following set of weights for the control points:

The ideas behind two dimensional cubic Bézier curves naturally extend to the third dimension – the curve can twist and turn as it goes through space:

We’re not just here to talk about curves, so let’s try to see how we can extend Bézier curves into surfaces.

# Bézier Patches[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#bézier-patches)

When we were creating a simple surface we were sliding a straight segment along some other two linear segments. We can expand this idea to slide a **straight segment** along two **cubic Bézier curves**:

While the surface itself is now more varied on the **purple edges**, it’s hard to hide the straightness of the **yellow segment**. To make things more varied we could replace that segment with a single cubic Bézier curve that we would stretch as we go, but by building up on the previous ideas we can do something much more interesting.

Firstly, we’ll introduce a set of _four_ cubic Bézier curves in the 3D space. Then we can use those **four curves** as rails on which **four control points** can slide. Those **control points** in turn define a **new Bézier curve** which in turn traces the final surface as it travels through space:

Notice that the **four black control points** aren’t directly controllable – they change their positions as they slide on the **purple rails** which in turn keeps changing the **dragged Bézier curve**. This process forms a cubic Bézier surface, or a cubic Bézier _patch_. That new surface is all together defined by 16 control points which can be arranged in a connected 4×4 grid:

As we’ve already seen, every point on that surface is first defined by evaluation across the set of **four Bézier curves** followed by interpolation on the resulting **new curve**:

Each point of the input square corresponds to some **point** on the surface. The surface distorts the straight lines on the input square into cubic Bézier curves in the 3D space:

The equation driving that surface is so massive that I’ll just represent the     parts using their triangular symbols:

P

=

P~11

×

×

×

×

×

×

+

P~12

×

×

×

×

×

×

+

P~13

×

×

×

×

×

×

+

P~14

×

×

×

×

×

×

+

P~21

×

×

×

×

×

×

+

P~22

×

×

×

×

×

×

+

P~23

×

×

×

×

×

×

+

P~24

×

×

×

×

×

×

+

P~31

×

×

×

×

×

×

+

P~32

×

×

×

×

×

×

+

P~33

×

×

×

×

×

×

+

P~34

×

×

×

×

×

×

+

P~41

×

×

×

×

×

×

+

P~42

×

×

×

×

×

×

+

P~43

×

×

×

×

×

×

+

P~44

×

×

×

×

×

×

The result of all of those 16 sets of triangular multiplications are 16 weighting functions that define how important the given control point is to the shape of the surface in the point’s vicinity:

Notice the symmetry in all those functions – ultimately there are only three unique shapes here, the others are their reflections and rotations.

# Beyond Cubic[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#beyond-cubic)

While relatively flexible, simple cubic curves and surfaces have their limitations. For example, a **cubic Bézier curve** can have at most two “bends” – it’s impossible to make it fit the **gray curve**:

One approach to solve this problem is to build more complicated Bézier curves by increasing the number of control points. Thankfully, our method of linearly interpolating the linear interpolations that we used to upgrade quadratic Bézier curves to cubic ones allows us to add arbitrary number of control points. In the demonstration below you can see how a Bézier curve with _eight_ control points is built:

On every interpolation step we reduce the number of intermediate points by one and after the 7^th step we’re down to our final point that defines the path. With a single Bézier curve with that many control points we can finally try to fit the shape:

Bézier curves with more control points provide better flexibility, but unfortunately they come with their own problems. Firstly, notice that to [fit the shape](#) the control points of the **curve** have to be put quite far apart making them slightly less convenient to use.

Moreover, changes to any of the control points causes the _entire_ curve to move. In the demonstration below I’ve enlarged a small section in the beginning of a **curve**. When you move the **selected** 6^th point, the section of the **curve** near the _2^nd_ control point changes as well:

When we look at the plot of the weight that each point has as we **progress** through the curve we can notice that, to some extent, they all contribute almost the entire curve:

Single Bézier curves with many control points lack the property of _local control_, making them not as useful for expressing more complicated shapes, so for better or for worse we have to rethink our approach to designing complicated shapes.

# Splines[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#splines)

Instead of using a single curve with many control points, we can use multiple curves with few control points. In the demonstration below I put three **cubic** **Bézier** **curves** that we can arrange to create more complex shapes:

While flexible, this setup is a bit cumbersome to use, as these three curves have gaps unless we [connect their end points](#). We can automate this connection process by having the last control point of the previous curve always match the first point of the next curve:

This solves the problem of gaps but if we’re aiming for nice, smooth shapes then we still have some sharp corners to account for. To remove the kinks we have to ensure that the _tangency_ of neighboring curves is continuous as well.

I’ve [discussed](https://ciechanow.ski/gears/#tangent--normal) tangency on this blog before, but, as a quick recap, a tangent is a local “straight ahead” direction. It can be easily found by sliding **two beads** on a **curve**. As the **beads** get closer, the line spanned through their centers approaches the tangent direction:

To ensure that the tangency of neighboring cubic Bézier curves is consistent the next _and_ previous neighbors of the joining control point have to lie on the same straight line. Many design tools tie the control points of neighboring curves together giving a single control axis that maintains the tangency. That entire utility is usually known as a _pen_ or _vector_ tool:

The curves we’ve built in this section are known as [_splines_](https://en.wikipedia.org/wiki/Spline_(mathematics)) which are piecewise polynomial curves – they’re constructed from different pieces, each one described by a polynomial function.

When it comes to designing complex surfaces, we can employ the same idea of using multiple cubic Bézier patches to form more complicated shapes. With the most basic setup those have the same continuity problems that individual curves had:

Notice how much work it is to have the two surfaces without any gaps. Thankfully, just like we did for curves, the edge points of neighboring patches can be tied together to make the seam water tight.

When it comes to tangency, the concept of a _single_ tangent direction doesn’t make that much sense for surfaces – at a given point the surface “goes” in many directions. To account for that we define an entire tangent _plane_. Similarly to what we did for curves we can take **three beads** and **three straight wires** attached to them and then slide those **beads** close to the **point** on the surface:

As the **beads** come to the target **point** infinitely close the three wires define the **tangent plane**. That plane also has a perpendicular direction which we call a _normal_ direction of the surface at that **point** – I’ve marked that direction with a **red arrow**:

For two surfaces to be connected without a sharp edge we need the normals at the joining edge to be aligned in the same direction:

Note that even when the surfaces don’t have any gaps it still requires a [lot of adjustments](#) to keep them connected and free of sharp edges. But that’s not even the end of the difficulties that joined patches create.

# Curved Mirror on The Wall[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#curved-mirror-on-the-wall)

It would be reasonable to think that removal of sharp edges is all it takes to create pretty surfaces, but when the surfaces are _reflective_ we still have some work to do. In the demonstration below you can see a mirror-polished surface reflecting a **red sphere**. By dragging the slider you can bend that surface into an arc of a circle, the **black curve** below shows a cross section of the mirror’s shape:

Notice that as the mirror pulls away from the flat shape the reflection of the sphere gets narrower. To get an intuitive understanding of why this happens we have to look at this situation from the side. The **black line** represents the mirror and the **red line** shows a reflection of the sphere in that mirror:

When the surface curves, its **normal directions** spread out. In simple terms, a curved mirror “sees” more of its environment but since the mirror’s area stays the same, the reflection of the sphere has to shrink to fit in.

When we bend the surface we’re actually changing the [_curvature_](https://en.wikipedia.org/wiki/Curvature) of the profile of the surface. Roughly speaking, curvature defines how quickly a curve changes its direction.

In the demonstration below I’ve marked curvy sections of the curve with different colors – the higher the curvature the more intense the color. Notice that this curve can bend in two different directions, so I’m using **orange** and **blue** to distinguish these cases. By dragging the **slider** you can witness how quickly the local direction of the curve, shown as a **black arrow**, changes in the areas of large curvature:

A [straight line](#) has no curvature and the arrow never turns, while a [tight turn](#) has a high curvature and the arrow turns very rapidly when passing through it. To show a more precise measure of a curvature we can use an [_osculating circle_](https://en.wikipedia.org/wiki/Osculating_circle) which conceptually is a circle that locally “fits” into the curve:

Curvature **κ** is the inverse of the radius **R** of that circle:

κ = 1 / R

That radius **R** is also known as the _radius of curvature_. Note that the inverse relation makes sense – a _small_ curvature implies a _not_ very curvy region which in turn implies _large_ radius of curvature. A curvature of a curve is also often visualized using a _curvature comb_:

Comb’s teeth are protruding in the normal direction of the curve and the higher a tooth’s length, the larger the curvature in that region.

Let’s look at _two_ reflective surfaces next to each other. I made their backs have different colors so that it’s easier to see where they join. The **top slider** controls the position of the sphere and the **bottom one** controls how closely the curvatures of the two surfaces match:

Notice that the connection doesn’t have any sharp edges. However, for different values of the **curvature match** the reflection of the sphere at the connection can look [weirdly deformed](#) into an UFO‑like shape, or it can be [quite smooth](#). If we analyze the situation from a side profile with a curvature comb visible we can get a clearer picture of what’s going on:

This view explains why in [some cases](#) the transition between the arched and the flat part of the surface has a visible jump in the sphere’s reflection – there is a _sudden_ transition between the area where the curvature is zero and the reflected image is not squeezed at all, and the area of non-zero curvature where the image is squeezed a lot. When we [fix that sudden jump](#), the reflected image becomes _gradually_ squeezed as it enters the curved part.

When curvatures between connected surfaces don’t match, the reflections may look very weird. _Curvature continuity_ is critical for achieving [high quality](https://en.wikipedia.org/wiki/Class_A_surface) reflective surfaces which are very commonly used e.g. on cars.

Even when surfaces are very far from being mirror-polished a rapid change in curvature may be observable:

Notice that in [some orientations](#) you can see a fairly sharp falloff in the shading on the surface. That transition gets much smoother if we [make the curvatures vary more smoothly](#).

Even though we were looking at light reflected off surfaces, we’ve actually been talking about the curvature of the _curve_ defining the profile of those surfaces. The notion of the curvature of a surface itself is a bit more complex, but in many cases it involves analyzing curvatures of curves living on that surface. Let’s try to look for some of those curves.

For every point on a surface we can take a **normal direction** and use it as pivot on which a **new plane** can rotate:

Notice that this **plane** slices the surface creating a curve at the cross section. We can then find the curvature of that curve at that **point** and show the osculating circle, or at least a part of it:

These curvatures are known as _normal curvatures_. Notice that at a given **point** a surface will have many curvatures, one for every direction of slicing. However, at every point there is a direction for which that curvature takes the **maximum** value, and a direction for which the curvature takes the **minimum** value. Note that the minimum value can be the _most negative_. Those two maxima are known as [_principal curvatures_](https://en.wikipedia.org/wiki/Principal_curvature). I’ve shown them in the demonstration below:

For some [cylindrical shapes](#), one of the curvatures will always be 0, but for [saddle-like surfaces](#) one will be positive and one negative. Moreover, the directions of two principal curvatures are always perpendicular to each other, but the reason for that is a bit [complicated](https://math.stackexchange.com/questions/71854/is-there-a-geometric-explanation-for-why-principal-curvature-directions-are-orth). The product of the two principal curvatures is known as [_Gaussian curvature_](https://en.wikipedia.org/wiki/Gaussian_curvature).

While the curvature discontinuity was easy to see on reflective surfaces, it’s quite hard to notice on regular 2D curves. However, in some cases we can actually feel it.

Trains and subway carts ride on railroads that can’t go on straight forever – at some point they have to change direction. One could naively think that a turn of a train’s track consists of an **arc of a circle** joining two **straight segments**. In the demonstration below I put a **little train** riding on that track. You can control the time using the slider:

The **red arrow** shows a [_centripetal force_](https://en.wikipedia.org/wiki/Centripetal_force) that makes the train and thus its passengers change direction. That **force** **F** depends on the mass **m** of the object, a square of its velocity **V**, and the radius of curvature **R** of the traveled path:

F = m × V^2 / R

On the straight part the radius of curvature is infinite so the force is 0, but when the train enters the circular part of our simple track the centripetal force suddenly appears leading to a very unpleasant jerk. That jerk is caused by the track’s curvature suddenly changing from a zero to a non-zero value. Real train tracks use [_transition curves_](https://en.wikipedia.org/wiki/Track_transition_curve) that smoothly vary the curvature between the straight and circular parts to avoid a sudden increase in forces which makes the ride much smoother.

Let’s sum up the different classes of continuities that we’ve discussed so far:

G0 position continuity

G1 tangency continuity

G2 curvature continuity

We can visualize them on two Bézier curves with curvature combs visible. Notice that as you enable higher degrees of continuity the movement of some of the control points becomes restricted:

While different tricks and affordances can be employed to maintain these continuities, we should look for a better way to design complex curves and surfaces – a method that has all these continuities built-in.

# Building the Basis[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#building-the-basis)

Let’s take a step back and look at the weights of the single Bézier curve with eight control points that we’ve already dismissed:

The problem with that approach was that the weight of each control point had a very far reaching range – it spans the entire progress of the curve. Let’s try to minimize how far reaching the impact of each point is by replacing it with simple triangular functions:

The weight of a control point is now non-zero only in a small range of the entire progress of the curve – each point has a minimized reach. Unfortunately, the resulting curve is not very impressive. While it doesn’t have any gaps, it forms just a plain polyline. The beauty of this approach, however, is that we can try using _better_ base functions with limited range.

One could be tempted to use an arbitrary shape for the individual weighting functions, for example, some smoother parabolas:

The results are completely janky. We’ve not only created some weird arcs, but also their shape and “sidedness” depends on where on screen the control points are.

To understand why this happens we have to look at the _sum_ of all the weighting functions over the entire range, I’ve visualized it using a thick **yellow line** on top of the plot:

Notice the resulting curve behaves weirdly in the regions where the weighting functions add up to more than 1.0, I’ve depicted that 1.0 margin with a dashed line. In those faulty ranges we no longer take a proper weighted average of some points, causing the broken behavior.

In fact, all the curves we’ve discussed so far had the property that all their weighting functions added up to 1 within the defined range forming a so called _partition of unity_. That concept is critical for the design of the weighting functions, as it makes the resulting curve behave as expected when all the control points are moved around as a group.

We could try to normalize the janky parabolas to make them nice, but in practice we’ll use so called [_B‑spline_](https://en.wikipedia.org/wiki/B-spline) functions that are very well behaved. The most primitive B‑spline function of order 1 has a value of 1.0 in a small range and 0.0 everywhere else as seen below. Higher orders of B‑spline functions are generated from two lower order functions, with a simple procedure that you can witness by dragging the slider:

In fact, our triangular function is a B‑spline function of [order 2](#). The [next order](#) forms a _quadratic_ B‑spline. Here’s a curve built using quadratic B‑splines as base functions:

The curve no longer has any unpredictable behavior and doesn’t have any sharp corners. In fact it has both position (G0), and tangency (G1) continuity. The fourth order B‑spline, known as a _cubic_ B‑spline, is even better – its curvature is also continuous making the entire curve G2 continuous:

The weighting functions of B‑splines have limited range so every control point only modifies the curve locally which solves the problems we’ve seen with complicated Bézier curves. However, you’ve probably noticed that for both quadratic and cubic B‑splines the curve no longer reaches the first and last control points. In some cases it’s not a problem, e.g. when the control points form a closed loop:

To solve the problem for open curves we can’t just allow the **progress** to go out of range since the weighting functions don’t add up to 1.0 there and we’ve already seen the problems that would cause. Instead, we have to modify the functions _inside_ that valid range.

Firstly, notice that the functions we’ve built were designed over a repeating, _uniform_ interval that I’ve been marking using small triangles  at the bottom. Those triangles represent so called _knots_ on which the individual weighting functions are built.

However, nothing prevents us from adjusting those intervals as we please, making their distribution _non-uniform_. In the demonstration below you can witness how the B‑spline rules create different functions when the **distance between knots** changes:

We no longer can simply shift the base function to the right and instead we have to build the individual functions all the way up from order 1 because each function may be defined over different interval of knots. With those rules in place, you can witness what happens to the end points of the curve as we adjust the **position of the knots**:

When the first four and last four knots overlap, a cubic B‑spline curve extends all the way to the boundary control points as desired. Additionally, the position of all the other knots can be adjusted too. In the demonstration below you can see what happens to the curve as we **perturb** the position of the _interior_ knots as well:

By moving three knots of a cubic B‑spline curve into a single location, we can achieve a sharp corner reigned by just a single control point. With uniformly distributed knots we’d need to overlap _three_ consecutive control points to get a sharp corner.

The curves we’ve been playing with are known as a _non-uniform_ B‑splines. However, the world of B‑splines has one more trick up its sleeve.

# B‑spline Extravaganza[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#b8209spline-extravaganza)

So far each of the weighting functions was equally important, but we can easily break that assumption by making some functions more important than others by changing their _relative_ weights. For example, witness what happens to the curve as we modify the **weight** of the 4^th control point that I’ve marked with a letter **D**:

As we change the weight of that function the shapes of all the others are adjusted as well. This ensures that all the weighting functions add up to 1 over the entire valid range which maintains the partition of unity. By combining the non-uniform knot distribution with arbitrary weights we create non-uniform _rational_ B‑splines, also known as [_NURBS_](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline). Notice that the weight of an individual function actually affects the _ratio_ of weights, thus the _rational_ name.

Interestingly enough, only rational B‑splines can represent an arc of a circle _exactly_. Plain B‑spline and Bézier curves can only approximate them.

The ideas behind the B‑spline curves naturally extend to surfaces as well. For example, here’s the simplest uniform and non-rational B‑spline surface defined by a mesh of 4×4 control points:

We can also build more complicated shapes by creating bigger rectangular grids of control points. When we tweak the position of the knots, we can make the surface go all the way to the edges of the control mesh:

While I’m not going to demonstrate it here, one can also adjust the weights of individual weighting functions which fully exploits all the features that NURBS surfaces offer.

NURBS curves and surfaces are very powerful and they have a lot of flexibility, but they still have their limitations when it comes to modeling shapes. Firstly, it’s quite difficult to cut holes in NURBS surfaces. One approach is to simply ignore some parts of the input square. In the demonstration below you can control the radius of the **red circle** that defines the region where we’re _not_ drawing the surface:

This operation is a bit cumbersome because achieving the desired shape of the hole on the surface requires tweaking the hole’s shape on the input square so that it looks right _after_ it’s deformed by the surface.

You may have also noticed that all the meshes of control points we’ve been dealing with were rectangular in nature. This heavily limits the types of surfaces we can create. For example, it’s impossible to express a surface like the one below using a single B‑spline surface without having to somehow manually stitch it at the edges:

However, the entire point of using B‑spline curves and surfaces was to ensure automatic continuity and smoothness in the first place. Let’s go back to the drawing board for the last time to devise a scheme that will help to solve all these problems.

# Cutting Corners[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#cutting-corners)

Instead of an actual drawing board let’s start with a clean sheet of paper instead. Those usually come in rectangular shapes, but if we wanted a piece of paper to have a nice rounded corner we’d have to do some work. One of the easiest ways to do it is to repeatedly **cut off** the sharp corners:

After just three iterations the corner is quite round already. We can use this corner cutting idea to chip away at the control polygon of a curve as well. In the demonstration below you can control **how many times** we did the corner cutting procedure and the **relative distance** at which the cut happens:

If we cut the corners [too little](#) or [too much](#) the final curve will still look quite jaggy, but for [intermediate values](#) the resulting polyline starts to look very smooth – even the sharpest corners are chiseled down after a few iterations. This concept of corner cutting was originally devised by George Chaikin and the resulting curves are known as _subdivision curves_.

A particularly interesting curve is generated when the cut [happens](#) 1/4 of the way into the straight segments. As it was later discovered, that scheme actually converges to a **curve** that is equivalent to a **quadratic B‑spline curve** defined by the same initial control points:

After just a few steps, the **subdivision curve** matches the **B‑spline curve** in the background. This is fantastic news, as it gives us yet another way to think about simple quadratic B‑spline curves – they’re obtained by repeatedly cutting off corners of their control polygon.

The cutting scheme we’ve used so far placed two new points on an existing edge, but that’s not the only choice we have. For instance, we can place a **new point** on an existing edge _and_ place another **new point** as a refinement of the existing vertex:

In this scheme the new edge point **E~new** lands right in the center of the edge, and the new vertex point **V~new** is a weighted average of the original vertex **V** and its previous and next neighbors **V~prev** and **V~next**. We can express that dependence using equations:

V~new =  × V~prev +  × V +  × V~next

E~new = 0.5 × V~prev + 0.5 × V~next

In some sense we’re still cutting corners, but our method is a bit more sophisticated now. Once again, there exists a [set of weights](#) that’s particularly important. The **curve** it generates in limit is a **cubic B‑spline curve**:

However, the beauty of subdivision curves doesn’t end here. Firstly, we can modify the subdivision rules for the “tail” control points so that their new vertex points don’t move at all – this makes the curve stick to its end points. Moreover, observe that we’re making the new vertex position be a weighted average of the positions of the old vertex and its two neighbors, but we can easily extend that scheme to include _all_ its neighbors. This allows us to handle branches and loops very easily:

In the vicinity of those branchy points the curve is no longer a B‑spline curve, as those can’t fork, but in the “regular” areas we still use the same subdivision rules that gave us the well-behaved cubic B‑splines functions. The subdivision curves _extend_ the power of B‑splines curves into more arbitrary connectivity. The real magic starts when we employ subdivision rules for surfaces.

# Subdivision Surfaces[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#subdivision-surfaces)

Inspired by Chaikin’s original work for corner cutting in a quadratic B‑spline, [Ed Catmull](https://en.wikipedia.org/wiki/Edwin_Catmull) and [James Clark](https://en.wikipedia.org/wiki/James_H._Clark) have [extended](https://people.eecs.berkeley.edu/~sequin/CS284/PAPERS/CatmullClark_SDSurf.pdf) these ideas to surfaces by creating [Catmull–Clark subdivision surfaces](https://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface). First, let’s see them in action starting with a simple mesh of 4×4 vertices and 9 quadrilateral faces:

After a few iterations the surface looks awfully familiar to the simplest cubic B‑spline patch we’ve seen before. In fact, after infinitely many subdivisions that surface _does_ turn into a cubic B‑spline surface.

The brilliance of Catmull and Clark was to come up with a subdivision scheme of a simple grid that in limit approaches the well defined B‑spline surfaces. Let’s try to understand the gist of their method.

Starting with a single cubic B‑spline patch defined by a 4x4 control grid, they wanted to find an equivalent 5×5 control grid that would define _the same_ surface. In other words, given the 16 control points  defining the **gray surface**, we’re looking for positions of the 25 **new** **control** **points** that would define a surface with the same shape:

The arithmetical procedures needed to be done aren’t particularly important here, but ultimately the new control points can be classified into three distinct groups that end up corresponding to original **faces**, **edges**, and **vertices**. Their exact creation rules are as follows:

- **new face points** – average of the **vertices** forming the face
- **new edge points** – average of the two **new face points** from neighboring faces and two **existing end points**
- **new vertex points** – weighted average of: the **existing vertex**, midpoints of all the edges touching that vertex, and all the newly created **face points** from faces touching that **existing vertex**

On those new points new faces are created and we once again have a set of vertices and faces, but this time they’re more refined. If we repeat that scheme over and over again the created faces of the control mesh will actually create a cubic B‑spline surface that the original control points defined:

The crucial invention here is that nothing about the rules for creating the new subdivided control mesh relied on how the mesh itself is connected! If you recall, NURBS surfaces were limited to rectangular grids. Catmull-Clark subdivision scheme also works when the vertices of the initial mesh have different number of neighbors – in the mesh below each vertex has 3, 4, or 5 neighbors:

Moreover, the initial faces also don’t necessarily have to be four-sided, the subdivision rules also work for meshes whose faces are triangles or more complicated polygons:

To express holes in a subdivision surface all we need to do is to _not_ create faces in some regions of its defining mesh, like in this mask from the very first demonstration in this article:

This example also has modified the subdivision rules on the edges to use cubic Chaikin subdivision rules. This ensures that the surface doesn’t recede from the edges of the initial control mesh like we’ve seen happen for a simple subdivided patch.

Subdivision surfaces make it very convenient to describe perfectly smooth surfaces using relatively simple meshes. To achieve sharper edges one can either move the points closer together, or use [extensions](https://graphics.pixar.com/library/Geri/paper.pdf) of Catmull-Clark subdivision scheme that allow specifying edge sharpness.

# Further Watching and Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#further-watching-and-reading)

[A Primer on Bézier Curves](https://pomax.github.io/bezierinfo/) by Mike Kamermans is probably the best resource on the web dedicated to Bézier curves. Over the course of the extremely detailed article the author goes over a myriad of topics related to the curves, some [very theoretical](https://pomax.github.io/bezierinfo/#matrix) and some [very pragmatic](https://pomax.github.io/bezierinfo/#arclengthapprox). The site truly is one of the internet’s gems.

For a more advanced set of videos on topics related to curves and surfaces I recommend Keenan Crane’s series on [Discrete Differential Geometry](https://www.youtube.com/playlist?list=PL9_jI1bdZmz0hIrNCMQW1YmZysAiIYSSS). Keenan is a [professor](https://www.cs.cmu.edu/~kmcrane/) at Carnegie Mellon University and over the course of his lectures he does an excellent job of explaining the concepts with well-made visual cues, while avoiding bogging the viewer down with _too_ much formalism.

Finally, [Curves and Surfaces for CAGD](http://www.farinhansford.com/books/cagd/) by Gerald Farin is a very good textbook on all the topics I’ve discussed here any many more. The author does a much deeper dive into the underlying mathematics and the formulas are accompanied by well written explanations.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/curves-and-surfaces/#final-words)

Ed Catmull later co-founded Pixar, and ever since the short film [Geri’s Game](https://en.wikipedia.org/wiki/Geri%27s_Game), subdivision surfaces have been used in all of Pixar’s movies. Catmull and Clark’s invention made it easier for great storytellers to express themselves through computer graphics.

I find it fascinating that simple rules of repeated linear interpolations of straight segments end up creating delightful Bézier curves. Every letter you read on this website was crafted using Bézier curves, the primary building blocks of fonts.

Designers who shape exteriors of everyday objects or tweak the shapes used in 2D graphics focus on the visual form of their creations, but their creative freedom is unlocked by carefully composed mathematical formulas that power various design tools. I think it’s charming that simple and unassuming equations end up creating beautiful curves and surfaces.
