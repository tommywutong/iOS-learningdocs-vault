---
title: Tesseract – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/tesseract/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:373530773ae30614'
translated: false
---

> 原文：[Tesseract – Bartosz Ciechanowski](https://ciechanow.ski/tesseract/)　·　Bartosz Ciechanowski

# [Tesseract](https://ciechanow.ski/tesseract/)

A cube is one of the simplest solids one can imagine. Over the course of this article I’ll try to explain how to expand it to the next dimension to obtain a _tesseract_ – a 4D equivalent of a cube.

The concept of a four dimensional cube may be a bit overwhelming, but by the time we’re done it should hopefully become more clear what the demonstration below is all about. You can drag the object around to view it from a different angle. The slider modifies the object itself:

What you’ve just interacted with was a rotated tesseract going through our three dimensional world, but before we understand why it looks the way it looks we have to start at the very beginning. The initial steps we’ll go through may be simple, but they’ll let us build an intuition about the way a 4D cube is constructed.

# Building Cubes[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#building-cubes)

We’ll start our discussion in a nihilistic way by describing a zero dimensional space. This space is quite limited, it has no axes and it consists only of a single location:

Since 0D space has no concepts of width, height, or depth, the only thing we can build in it is a lowly point:

This isn’t particularly exciting, but we have to start somewhere and a point is the simplest geometrical object there is.

We can expand on that dimensionless space by adding an actual x dimension to it to obtain a 1D space. This world allows a bit more creativity. In the demonstration below you can take a single point and “stretch” it into the next dimension by dragging the slider:

We’ve just created a line segment. Notice that a line segment is bounded by two points, they define the extent of this new object.

Let’s expand our field of view to a more familiar two dimensional space by adding the y axis. Once again, we can perform the operation of taking the existing line segment and stretching it into the new dimension. We’ll use the same stretching distance as before to make things uniform:

We ended up with a square which is bounded by four line segments. Those segments in turn meet at four corner points. It’s worth pointing out that the new axis we added to represent the new dimension is [perpendicular](https://en.wikipedia.org/wiki/Perpendicular) to the previous one – a movement in the y direction is completely independent of a movement in the x direction.

We can continue the expansion process into the three dimensional space we live in. In the demonstration below I changed the viewing angle so that we can see how a square is stretched in the direction of the z axis:

By stretching a square into the third dimension we’ve obtained the classic cube. It’s bounded by 6 squares, which are bounded by 12 line segments, which in turn are bounded by 8 corners. We can finally view the familiar 3D cube with some perspective to help with depth perception. You can drag it around to see it from other directions:

In a three dimensional space all three xyz axes are perpendicular to each other. Unfortunately, there are some cases when this may not be particularly easy to see, so before we continue expanding the cube we need to take a quick sidestep to discuss those difficulties.

# Ambiguous Representation[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#ambiguous-representation)

You’ve probably seen a 3D coordinate system represented by a 2D drawing in one way or another. Below you’ll find a very common way to do it. I put a single black point in the 3D space, you can control its position with a slider:

Despite the movement of the point in a 3D space its position in a 2D drawing doesn’t change. A 2D representation of a 3D space is inherently ambiguous – it’s impossible to differentiate position of some points from the others.

Additionally, the 2D projection has skewed the angles between the axes. In the simulation they’re 120° apart, but we know that those angles are equal to 90°.

The crucial point here is that an attempt to represent a higher dimensional space using a lower dimensional space will always have its compromises. With those limitations in mind, let’s talk about a 4D space.

# Fourth Dimension[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#fourth-dimension)

We’ve seen how adding a higher dimension requires creating an axis perpendicular to all the other axes. The procedure to create the fourth dimension is no different. We’ll label the axis of this new dimension as w. Below you can interact with _one_ way to show a 4D space. You may drag the diagram around to change the viewing angle, I’ve also put a single point in that space:

Similarly to the previous example the position of the black point is ambiguous. Using the segmented control you can show the point at three locations in the 4D space:

A (1, 1, 1, 0)

B (0, 0, 0, −1)

C (2, 2, 2, 1)

Without the guidance of the helper lines it’s impossible to _univocally_ tell what the point’s coordinates are. Moreover, the angles between the axes literally don’t look right. This is particularly visible when we put a simple 3D cube spanned on xyz axes in a 4D space:

All four axes are actually perpendicular to each other, but we have no way of expressing that in a 3D model. To show that w axis is indeed at 90° to the other three, we have to ignore one of the dimensions and show all four possible triplets of the axes:

Both the angular deformation and position ambiguity are the result of a presentation of a 4D space using a 3D model. This is something that we’ll have to, at least temporarily, live with.

# Tesseract[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#tesseract)

So far whenever we were building a higher dimensional object we just took what we had and we stretched it into the new dimension. We’ll continue this process into the fourth dimension. In the demonstration below I made the walls of the cube transparent to show how the new edges are being formed. By dragging the slider you can stretch a cube to create a tesseract:

I personally find it quite difficult to see what’s going on with this form of presentation. Unfortunately, I don’t think I can do a better job of showing all four dimensions at once. Our human brains are hardwired to understand things in three dimensions – reasoning about the fourth one requires some amount of imagination or even delusion. We can try to understand how things work in 4D, but I don’t think we can _fully_ experience it.

However, not all is lost! I’ll show you some ways to remove one dimension from a 4D space and we’ll be able to use our perfectly 3D-capable brains to look at a tesseract from a different perspective.

# Stepping into the Shadows[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#stepping-into-the-shadows)

If you’ve ever played with shadows cast by the Sun or a flashlight, you may have noticed that they don’t really preserve the depth – they _flatten_ three dimensional objects into two dimensional figures. In fact, shadow casting is one of the ways of reducing the dimensionality of a space.

Let’s look at the relation between a plain 3D cube with semitransparent walls and its shadow. In the simulation below you can rotate the cube on the left side to see how its shadow changes. The light source is symbolized with a yellow dot on the far left side. The right side represents the direct view of the xy plane. You can choose to highlight one of the faces using the control underneath:

There are many interesting observations to be done here:

- A 3D cube projected onto a 2D space creates a 2D image
- Perfectly square faces of the cube are often deformed into [quadrilaterals](https://en.wikipedia.org/wiki/Quadrilateral)
- Intersections [may appear](#) between the edges, but in the cube the edges don’t intersect with each other, they just meet at the corners
- In [some orientations](#) it looks as if one of the faces encompassed all the others even though all faces are the same

The important point here is that a projection that creates a shadow introduces some distortions into the final image. By having some understanding of how the projected object is constructed we can at least _attempt_ to see through those flaws.

This next sentence requires a leap of faith. Just like a projection of a 3D object onto a 2D space creates a 2D object, a projection of a 4D object onto a 3D space forms a 3D object. In other words, a “shadow” of a tesseract is _three_ dimensional.

Without further ado, here’s a demonstration of that shadow with a light source put somewhere on the w axis. You can drag the shadow around to see it from different angles. The faces of the tesseract are tinted a little so that it’s easier to see which parts are in front. The segmented control below allows you to select different subcomponents of the tesseract:

The eight selectable solids are actually eight perfect cubes that form the tesseract. Many of them are deformed and don’t look like cubes at all, but we’ve already seen how a projection can skew squares into trapezoids and a similar thing happens here with the cubes.

Additionally, the eighth cube seems to encompass all the others, but again, that’s just a result of the projection. Each one of the eight cubes creating a tesseract is exactly the same. Moreover, each cube shares its faces with six other cubes, for example cube **1** neighbors with every other cube but cube **8**.

With that projection we can make some interesting observations about ways things are connected inside a tesseract. There are 16 vertices total and each vertex belongs to 4 edges and 6 faces:

A tesseract has 32 edges and 24 faces. Each edge belongs to 3 faces:

If you look back on the regular 3D cube you may recall that in a cube each vertex belongs to 3 edges and 3 faces, and each edge belongs to 2 faces:

As you can see a tesseract is just a cube on steroids, similarly to how a cube is an upgraded square, and a square is a next level line segment. A generalization of a cube in other dimensions is called a [hypercube](https://en.wikipedia.org/wiki/Hypercube). Here are the five hypercubes we’ve encountered:

0D point

1D line segment

2D square

3D cube

4D tesseract

The diagrams get very messy very quickly so I won’t show you any examples of higher dimensional hypercubes. However, the rules of building the subsequent hypercubes are exactly the same – take the previous hypercube and _stretch_ it into the new dimension. Every point creates a line segment, every line segment creates a square, every square creates a cube, and so on.

# Plane of Rotation[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#plane-of-rotation)

So far we’ve been looking at a simple case of an axis aligned tesseract and we’ve merely been viewing its shadow from different angles. The real fun begins when we _rotate_ a tesseract in a 4D space, but that requires talking about rotations in general.

In a 3D world you’re probably used to a concept of an _axis_ of rotation. In a rotating object, the only stationary points are those on the axis itself, the other points rotate _around_ this axis:

Equivalently, that axis can be used to define a _plane_ of rotation. Every point on that plane will paint a circle around the center point. Additionally, every plane parallel to that plane is just a sibling plane of rotation:

In a 3D world we can define three basic planes of rotation spanned between the axes of the coordinate system: xy, xz, and yz. Naturally, the plane of rotation can be positioned arbitrarily in the 3D space, but those three planes form the simplest building blocks:

The idea of a plane of rotation works well in 2D where the entire space is constrained to just a single xy plane. It lets us avoid the quirk of having to introduce a third dimension just to define an axis of rotation in that space.

A plane of rotation also works well in 4D where we can describe a total of _six_ basic planes – xy, xz, xw, yz, yw, and zw:

In fact, in four dimensions we can’t even _define_ an axis of rotation since every plane has _two_ different directions perpendicular to it. For instance, both z _and_ w axes are perpendicular to the xy plane. When a four dimensional object rotates in the xy plane, all points on the zw plane remain stationary.

The main takeaway here is that a plane of rotation is a more universal way of describing rotations since it works in 2D, 3D, 4D, and higher dimensions. We’ll use this concept to give the tesseract a spin.

# In-N-Out[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#in-n-out)

This next demonstration will be a little trippy, but dragging around to change the viewing angle will do wonders for understanding what’s going on. The slider controls the rotation of the tesseract in the xw plane. I highlighted one of the cubes to make it easier to see how it morphs:

You may notice that sometimes the faces of the tesseract seem to intersect, however, this is just a limitation of the projection. We’ve already seen a similar issue with edges of the 3D cube intersecting in its 2D shadow. In the actual tesseract those walls are perfectly disjoint.

The transformations of the highlighted cube may seem peculiar, but we can witness something very similar in a 3D cube and its shadow:

Notice how the yellow wall starts on the inside as a [square](#), then it moves to become an [interior trapezoid](#), only to degenerate into a [line segment](#), to come back as a [trapezoid](#) again, and to finally [devour](#) the entire object.

A rotating tesseract is an alien construct and we have no evolved intuitions about how it should behave, so don’t be afraid to fallback to a 3D cube in the search for explanations of the tesseract’s unusual nature.

# Leaving Plato’s Cave[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#leaving-platos-cave)

Playing with a shadow of a tesseract let us look into its structure, but it doesn’t illustrate how _we_ would perceive a solid tesseract traveling through space.

We’ll once again build some intuitions at a lower dimension so let’s see what happens when a 3D cube travels through a 2D world. In the simulation below you can drag the slider to change the cube’s position on the z axis. The right side shows a direct view of the xy plane. You may also drag the cube on the left side to change its orientation in the space:

Notice that when the cube is [perfectly aligned](#) with the axes it can pop in and out of existence on the 2D plane quite abruptly. A [simple rotation](#) in the xz plane creates a growing, shifting, and shrinking rectangle. In general case, a slice of an [arbitrarily rotated](#) cube creates a convex [polygon](https://en.wikipedia.org/wiki/Polygon). You can even create a [perfect hexagon](#).

For the grand finale of this article let’s drag a tesseract through a 4D space and see how it intersects with a 3D world. Just like an intersection of a 3D object with a 2D space creates a 2D object, an intersection of a 4D object with a 3D space creates a 3D object.

Behold the sliders galore! The first one controls the position of the tesseract along the w axis. The other three rotate the tesseract in xw, yw, and zw planes respectively:

Similarly to the 2D intersection of a 3D cube, when a tesseract [is axis aligned](#) it will abruptly pop in and out of existence when dragged along the w axis. A [simple rotation](#) about one of the planes spanned on the w axis will cause the intersection to be a growing, shifting, and shrinking [rectangular cuboid](https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid). A more [complex rotation](#) creates a more complicated shape – a convex [polyhedron](https://en.wikipedia.org/wiki/Polyhedron).

The anatomy of the 3D “slices” of a tesseract may seem bizarre, but we’ve already seen very similar patterns in 2D slices of a regular cube. This time they’re just one dimension richer.

It’s quite unlikely that you’ll ever get to interact with a real tesseract, but these examples have hopefully let you build some intuitions about what to expect in that fantastic scenario.

# Further Watching and Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#further-watching-and-reading)

[Marc ten Bosh](https://marctenbosch.com) does amazing things with the fourth dimension. His [4D Toys](https://marctenbosch.com/news/2017/06/4d-toys-a-box-of-four-dimensional-toys/) is a fully interactive app that allows you to play with four dimensional objects including physical interactions between them! His upcoming game entitled [Miegakure](https://miegakure.com) will explore these concepts in even more depth. Marc’s [explanation](https://www.youtube.com/watch?v=9yW--eQaA2I) of how walking through a 4D space works is well worth the watch.

For a short video about projections of a rotating tesseract I recommend [Understanding 4D – The Tesseract](https://www.youtube.com/watch?v=iGO12Z5Lw8s). James Schloss goes over a few things I’ve discussed here while also providing some more mathematical background on how to apply projections.

[Introduction to the fourth dimension](http://hi.gher.space/classic/introduction.htm) is a multi-part article about the concept of a 4D space. The website also [explores](http://hi.gher.space/classic/sitemap.htm) many of the unusual features of a higher-dimensional worlds. The site’s [forum](http://hi.gher.space/forum/index.php) is one of those hidden places on the internet that make you realize some rabbit holes are _really_ deep.

Chris McMullen’s book [The Visual Guide To Extra Dimensions](https://www.amazon.com/Visual-Guide-Extra-Dimensions-Higher-Dimensional/dp/1438298927/) provides a more thorough look at the fourth dimension. The author describes some other higher-dimensional solids and goes into more details about a hypothetical 4D universe.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/tesseract/#final-words)

I find it very inspiring that while we can’t physically experience a four dimensional space, with just a bit of ingenuity we can easily simulate how a tesseract and its shadow would look in our day-to-day world.

You may find math’s indifference to the limitations of our human perception quite cruel, but I think it’s liberating. Reflecting on higher dimensions is transcendent – it removes the shackles of the physical world and allows us to explore the realms we’ll never encounter.

Analyzing a tesseract may be of little practical use, but it hopefully stretched your mind into the fourth dimension at least to some degree.
