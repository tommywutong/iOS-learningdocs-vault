---
title: Naval Architecture – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/naval-architecture/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2676db66be0ccafe'
translated: false
---

> 原文：[Naval Architecture – Bartosz Ciechanowski](https://ciechanow.ski/naval-architecture/)　·　Bartosz Ciechanowski

# [Naval Architecture](https://ciechanow.ski/naval-architecture/)

When I first heard the term [_naval architecture_](https://en.wikipedia.org/wiki/Naval_architecture) I thought it was the artistic practice of designing beautiful boats. It turns out it’s a proper scientific discipline dedicated to the engineering of ships.

Over the course of this article we’ll go over different aspects of naval architecture. I’ll explain how ships are propelled, what makes them stay afloat, and how they’re carefully designed to not tip over even in dynamic conditions:

To understand why a ship rocks side-to-side in the wavy ocean waters, we first have to understand that it’s water itself that’s responsible for all of the ship’s behaviors. We’ll start with a simple device – a water-filled syringe.

# Pressure[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#pressure)

You’ve probably seen a syringe before. When its plunger is pressed, the contents of the syringe come out on the other end. In the demonstration below we have a syringe connected through a thin hose to another container that has a spring in it. The entire system is filled with **water**. As you increase the **force** on the plunger observe the little spring being compressed at the other end of the hose:

By applying **force** on the plunger we increase the _pressure_ in the **fluid**, which in turn pushes the little piston and compresses the spring. We can measure that pressure using a pressure gauge. In the demonstration below the sliders allow you to control the applied **force** and the **area** of the plunger:

Observe that the pressure **P** on the gauge is proportional to the perpendicular input force **F**, but it’s inversely proportional to the area **A**. We can tie these three values using the following equation:

P =  F / A

In metric system pressure is expressed in _pascals_ (Pa) named after [Blaise Pascal](https://en.wikipedia.org/wiki/Blaise_Pascal), while in the imperial system _pounds per square inch_ (psi) are commonly used.

Notice that we no longer have any spring to compress. Even though we’re applying a force the plunger doesn’t move since water, unlike air, is [minimally compressible](https://en.wikipedia.org/wiki/Properties_of_water#Compressibility). It’s easy to squeeze an empty, tightly screwed plastic bottle, but when filled to the brim with water the bottle won’t budge much. At the pressures we’re applying here, water practically doesn’t change its volume.

With a syringe, we’ve directly applied a force by pushing on the plunger, however, we could recreate that experiment by putting a heavy, tightly fitting **weight** on top of **water** in a container. In the demonstration below you can control how heavy the **weight** is to see how it affects the pressure read by the gauge:

Note that even when we [remove the weight](#) the pressure meter shows a non-zero read. The water itself also has weight so its mass above the point of measurement contributes to the readout as well.

Let’s try to quantify the force exerted by the water. Firstly, notice that the shape of the water above the measurement forms a cylinder with height **h** and a base surface area **A**:

The mass **m** of that cylinder of water is just its volume **V** times the density **ρ** of the contained water:

m = ρ × V

That highlighted volume **V**, however, can also be expressed as the area of the base **A** times the height **h** which we can plug into the equation for mass **m**:

m = ρ × A × h

The force of gravity **F** acting on that water is equal to its mass **m** times the gravitational acceleration **g**:

F = m × g

If we now plug all these values to the equation for pressure **P = F / A** we get:

P =  ρ × A × h × g / A

Which we can simplify by reducing the area **A** to obtain the final equation for pressure **P** of liquid with density **ρ** at a depth **h** under surface:

P = ρ × h × g

Note that the resulting pressure **P** is independent of the base area, it’s only affected by the height **h** and density **ρ** of the water above:

In general the density **ρ** of water is not constant and depends on temperature and [salinity](https://en.wikipedia.org/wiki/Salinity), but at the scales we’re interested in we can assume its value doesn’t change.

If you recall our first demonstration of a loaded syringe, you may remember that the pressure applied to the plunger “travelled” through the hose to act on a spring, which was quite distant from the syringe itself. The very same rules apply here. Observe the pressure shown by the gauge two different spots of this L-shaped container:

The right gauge always shows the same pressure even though in some cases there is less water “directly” above it. This may seem a little surprising, but you’d probably agree that if we removed the **green plug** from the [filled](#) container, the water would come out of the opening because of non-zero pressure in that area.

That behavior of pressure in incompressible fluids is known as [Pascal’s law](https://en.wikipedia.org/wiki/Pascal%27s_law). It states that pressure applied to any part of the liquid will be transmitted in all directions. As a result, the pressure in a connected body of water is the same at every level under the free surface.

It’s worth stressing that in these static cases the pressure at a given level depends _purely_ on the height of the body of water. This may have some unexpected consequences. For example, pressure at the bottom of these two containers is _exactly_ the same:

Note how much less water there is in a thin straw compared to the wide container. This scenario is known as _Pascal’s barrel_. By making the straw longer and filling it with water we can make the pressure inside the barrel arbitrarily large, causing it to explode. While Pascal himself possibly [never performed](https://en.wikipedia.org/wiki/Pascal%27s_law#Pascal's_barrel) that experiment, some modern recreations [have been successful](https://www.youtube.com/watch?v=EJHrr21UvY8).

# Buoyancy[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#buoyancy)

On its own pressure doesn’t have any direction – it’s a _scalar_ value, just like temperature is. However, the force exerted by pressure acts in the normal, that is locally perpendicular, direction to the surface of the object. We can visualize the local forces created by the pressure with small arrows:

In fact, these forces act not only on the container itself, but also on any object placed in the water as well. In the demonstration below a **red brick** is hanging on a **string**. You can dunk it into water using the slider:

From this point on I’ll remove the constraints of containers and we’ll instead move outdoors where we’ll submerge things into vast, peaceful ocean waters. In this new environment the rules of pressure remain the same – after all, we’re still dealing with water.

The brick is now hanging on a string that is attached to a scale, which we’ll lower. Notice that as a larger part of the brick gets underwater, the weight shown by the scale decreases:

While the horizontal arrows of water pressure forces balance each other, the vertical ones don’t, and the pressure exerts a net positive force that pushes up on the brick. All the small arrows add up to the cumulative force known as [_buoyancy_](https://en.wikipedia.org/wiki/Buoyancy). In this example **buoyancy** is not strong enough to completely overcome the force of **gravity** acting on the brick, but it manages to diminish it to some extent, which reduces the weight as measured by the scale:

Note that for the sake of clarity, I shifted the arrows apart a little, but in this simple scenario **buoyancy** and **gravity** are actually positioned on the same vertical line.

If we use a wooden block instead of a brick, the situation changes a bit. As the block gets gently lowered, it will reach a point where the water is capable of keeping it on the surface and the string gets some slack:

If we remove the string and manually push a wooden block underwater, the force of **buoyancy** will become higher than the block’s **weight**. When we let go of the block, the water will push it up:

Once the block gains some speed it may even overshoot its steady position, only to get pulled down by **gravity** again. After a while the water resistance slows the oscillating movement enough for the block to find its steady balance.

Let’s try to quantify the force of **buoyancy** as created by the pressure. Naturally, the forces here are three dimensional, however, observe that all the **horizontal** components are matched on the opposite side and they cancel each other out. Only the pressure forces on **top** and **bottom** are unbalanced. You can drag the block around to see all the pressure forces acting on it:

The pressure **P**~**T** on **top** of the brick acting on the **top** surface area **A** exerts the force **F**~**T** equal to:

F~T = P~T × A = ρ × g × h~T × A

Similarly, the resulting force **F**~**B** acting from the **bottom** is:

F~B = P~B × A = ρ × g × h~B × A

And the net force of buoyancy **F** in the upwards direction is the difference of the two:

F = F~B − F~T = ρ × g × (h~B − h~T) × A

Notice however, that the highlighted difference is just the height of the submerged part:

F = ρ × g × h × A

And the product of height **h** and the base area **A** is volume **V** of the submerged object, which gives us the equation that ties the force of buoyancy to the _displaced_ volume **V** of fluid with density **ρ**:

F = ρ × g × V

Displaced volume is the volume of fluid that would normally occupy a space that is now filled by the object. We can also observe that density **ρ** times volume **V** is just mass **m**:

F = m × g

This is force is just the weight of the displaced fluid. This general rule, known as [Archimedes' principle](https://en.wikipedia.org/wiki/Archimedes%27_principle), states that the force of buoyancy is equal to the _weight_ of the fluid that the object has displaced. Note that buoyancy does _not_ depend on the weight of the object itself, it’s only affected by the _submerged_ volume of that object.

You may wonder if the same rule holds for an arbitrary shape. After all, I’ve conveniently used a plain wooden block to simplify the volume and force calculations. However, we can use the same method even for smooth shapes by subdividing them into arbitrarily small rectangular prisms.

In the following demonstration you can use smaller and smaller prisms to approximate the shape of a sphere. For the sake of clarity, I’m only coloring the **top** and **bottom** surfaces. You can drag the simulation around to see it from different angles:

Notice how quickly a group of blocks starts to resemble the smooth shape of the sphere.

Now that we know that the force of buoyancy depends on the submerged volume we can also analyze what happens when the wooden block is forcefully tilted:

The local forces exerted by pressure are no longer symmetrical so they end up having an uneven effect on the body. At a first glance it may be hard to figure out what the cumulative effect of all those small arrows is. However, just like we can simplify the weight of all particles constituting an object to a single gravity force acting on its center of gravity, we can also simplify the local forces of pressure acting on the surface of an object to a single buoyancy force acting through a _center of buoyancy_, which I’ve visualized using a **small blue circle**:

As it turns out, the center of buoyancy is just the center of gravity _of the displaced water_. Note that the **force of buoyancy** may not be aligned with the **force of gravity** of the object. That misalignment of forces will create [torque](https://ciechanow.ski/gears/#torque) causing the object to rotate until it finds its equilibrium, which happens when the forces of **gravity** and **buoyancy** are aligned.

# Hull[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#hull)

In some sense, the floating block of wood we’ve seen so far forms a very simple ship – a [_raft_](https://en.wikipedia.org/wiki/Raft). It’s not a very practical vessel, as it has small cargo carrying capacity. We also want to make sure that a ship can withhold the elements, so ideally we’d use more robust materials. A solid block of steel won’t float on its own because its weight is much larger than the force of buoyancy acting in it. However, if we hollow out the inside of the block we’ll significantly reduce its mass while maintaining the volume:

What we see here is a very simple _hull_ – the main body of a ship. This tub-like body is now capable of floating, despite being made from steel. Note that this ship behaves very similarly to the wooden block:

This is ultimately how a ship floats. The weight of water it can displace is larger than the weight of the ship itself causing **gravity** and **buoyancy** to balance each other. While this hull shape is used on [_barges_](https://en.wikipedia.org/wiki/Barge), the hull of a typical modern ship looks more like the one in demonstration below. You can drag it around to change the point of view:

This hull is covered with a [_deck_](https://en.wikipedia.org/wiki/Deck_(ship)), but some smaller boats may have an open top. The front part of the ship is called a [_bow_](https://en.wikipedia.org/wiki/Bow_(watercraft)). This hull has a [_bulbous bow_](https://en.wikipedia.org/wiki/Bulbous_bow) which is the “nose” in the front bottom part – for larger ships it improves the flow around the ship, reducing drag. The back of the ship is called a [_stern_](https://en.wikipedia.org/wiki/Stern). The left and right side of a ship are respectively called [_port and starboard_](https://en.wikipedia.org/wiki/Port_and_starboard). The fin-like object in the back called a [_rudder_](https://en.wikipedia.org/wiki/Rudder) is used to steer the ship. The fan-like device next to it is a [screw propeller](https://en.wikipedia.org/wiki/Propeller), which, when rotated by an engine, pushes the ship forward.

Most ships have a streamlined shape, which reduces the resistance of motion when sailing as the bow can part water more easily. Other than drag considerations, it may seem that the shape of the hull can be more or less arbitrary. However, naval architects have to consider another very important factor – the stability of the ship.

# Stability[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#stability)

So far all of the bricks and wooden blocks have been floating in pristine conditions, but in practice open waters are very rarely perfectly calm. Disturbances caused by waves and wind will usually rock the hull from side to side a little:

If you look at the ship [from the front](#), you can see the so called _angle of heel_, which defines how far a vessel is tilted away from vertical. This front view will be very important for our considerations.

Firstly, let’s see how the proportions of the hull affect the behavior of the ship when external forces are applied. In the demonstration below, the **first slider** controls the wind, which will tilt the ship one way or another. The **second slider** changes the proportions of the hull:

For [relatively wider shapes](#) the ship tilts a little [due to wind](#), but it finds its stable position and will return back to vertical when the [wind stops](#). For [more vertical shapes](#), however, the ship will tilt and [_capsize_](https://en.wikipedia.org/wiki/Capsizing) even when the [wind stops](#). For most ships this is a catastrophic condition.

To understand what’s going on, we need to look how the force of **gravity** and **buoyancy** act on a tilted hull. As we’ve seen before, when the ship is **tilted** the two forces are separated by a certain distance shown below in **white**:

That **white line** is the _righting arm_, which is the horizontal distance between the two forces. The force of **buoyancy** acting through this **arm** exerts a rotating torque on the ship. The curly arrow at the top shows the direction of the turn. For a [short and wide](#) cross section of the hull, the force of **buoyancy** acts against the tilt of the ship, helping to straighten it up. For a more [vertical shape](#), however, the **buoyancy** acts _with_ the tilt of the ship, causing it to rotate even further!

We can visualize the length of the righting arm for different heel angles of the hull using the following plot. When the **angle of heel** is in the **green zone**, buoyancy helps the straighten the ship. However, if the **ship’s angle** is in the **red zone**, buoyancy tries to _heel_ the ship even more:

Some hull shapes are inherently _unstable_. The slightest deviation from pristine vertical balance will make the ship [flip](#). However, even hull shapes that are initially stable at some angle [reach their limits](#). All of these examples assume the deck is perfectly sealed and that water doesn’t get into the hull.

Moreover, it’s not just the rectangular proportions that affect the stability of the hull. The ship’s safety is also affected by its cross-sectional shape:

At first glance it may appear that less rectangular, slimmer shapes are inherently better. However, many ships are expected to operate only at reasonable **angles of heel** out of concern for the safety of passengers and cargo. Within that range the stability is comparable. Additionally, bulky, rectangular hulls allow much higher cargo loading capabilities.

Another way to look at stability is to consider the [_metacenter_](https://en.wikipedia.org/wiki/Metacentric_height#Metacentre), which lies at the intersection of the vertical from the original center of buoyancy with the vertical from the **heeled** center of buoyancy. I visualized that intersection with a **white dot**:

As long as the **metacenter** stays above the center of **gravity** then the heeled ship will try to return to vertical.

Naval architects designing the hull have to ensure that the ship will remain stable across the expected spectrum of angles. Some ships, such as sailboats, are designed to handle a much higher critical angle of heel, but their construction also employs a trick of lowering the center of gravity by using additional weight attached below the hull. This ensures that the metacenter can stay above the center of gravity for a much larger range of angles.

While a ship and its machinery have a relatively fixed mass and position this unfortunately can’t be said about the cargo it carries.

# Cargo[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#cargo)

Most ships sailing on ocean waters carry some sort of cargo, quite often packed in [standardized shipping containers](https://en.wikipedia.org/wiki/Intermodal_container). Let’s analyze what happens to the ship as we load it up. In the demonstration below, we’re looking inside the ship. You can control both the **n****u****m****b****e****r** and **vertical position** of the containers:

As containers are added the ship will sink a little and increase its [_draft_](https://en.wikipedia.org/wiki/Draft_(hull)) – the distance between the bottom of the hull and the [_waterline_](https://en.wikipedia.org/wiki/Waterline). A new balance is created between the increased weight due to the cargo and the increased buoyancy due to larger volume of the submerged part. However, if the heavy cargo is [placed too high](#), the ship will spontaneously capsize after some time.

Let’s analyze how a change of the vertical position of containers on a big ship affects its **center of gravity** and thus the stability curve:

If the cargo is placed [relatively low](#), it can actually significantly increase the stability of the ship. However, for [some positions](#) of cargo, the ship’s stable position is tilted to one side or the other, even though the geometry of the hull and carried load are perfectly symmetrical – that angle is known as [_angle of loll_](https://en.wikipedia.org/wiki/Angle_of_loll). When the cargo is placed [very high](#) this ship becomes completely unstable.

Naturally, when the cargo itself is not horizontally balanced the ship will also find a stable _tilted_ position, which you can witness in the demonstration below. The slider controls the horizontal position of the **heavy box**:

Once again, the ship will find its static equilibrium at some angle, known as [_angle of list_](https://en.wikipedia.org/wiki/Angle_of_list), which this time is caused by the lateral imbalance. You may have experienced that tilting when you lean on a side of a small rowboat or a kayak.

So far we’ve been keeping the cargo in place, either locked into slots, or tied down to ship itself. However, if we let this **heavy box** slide the results can be truly catastrophic:

As the ship tilts at some point the friction between the **cargo** and the floor isn’t high enough to keep the box in place and it [starts to slide](#). This in turn shifts the center of gravity of the ship farther to the side, which causes even bigger tilt. Even when the [wind stops](#) the ship won’t return to vertical. We can clearly see how unavoidable the problem becomes on the diagram:

Heavy cargo on a ship has to be locked in place so that it doesn’t change the ship’s balance. While it’s relatively easy to do for boxes, crates, and containers, some forms of cargo are more difficult to tame.

# Free Surface[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#free-surface)

A [tanker ship](https://en.wikipedia.org/wiki/Tanker_(ship)) can be used to carry chemicals, crude oil, or even [orange juice](https://en.wikipedia.org/wiki/Atlanship_SA). Notice what happens to this tanker ship as it tilts with the **wind**. You can also change the level of **liquid** in the tank:

Once the ship [starts to tilt](#) the **liquid** inside will move to the side as well, which changes the center of gravity of the ship, which causes even further tilt. Even when the [wind stops](#) the ship won’t return to the straight position. However, the [opposite wind](#) may be able to move the ship to the other extreme. It’s worth pointing out that neither [empty](#) nor [full](#) tanks exhibit this problem.

This [_free surface effect_](https://en.wikipedia.org/wiki/Free_surface_effect) is very dangerous for the ship’s stability. Even ships that aren’t purposely carrying liquid cargo still have to keep fuel and ballast water on board. Moreover, small, bulk materials like sand, gravel, and grains also exhibit a fluid-like behavior and will move around when the relative direction of gravity changes. One of the most straightforward solutions to this free surface problem is to separate the liquid into multiple compartments. This severely limits the movement of the liquid making the ship much more stable:

Free surface effect also creates particularly dangerous conditions when a ship’s hull is breached and water starts flooding the vessel. The heavy tilt can make the evacuation efforts of the crew and passengers much more difficult despite the ship still being technically afloat.

# Waves[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#waves)

For the final discussion of stability let’s look at the ship in waves. For prettier visuals we’ll top our hull with a [_bridge_](https://en.wikipedia.org/wiki/Bridge_(nautical)) – a platform from which a ship is commanded. The slider controls the amplitude of the waves:

Notice that as the wave passes through it changes the size and position of the underwater volume of the hull, which in turn shifts the **center of buoyancy**, causing the ship to tilt.

Every ship has its natural roll frequency, which determines how quickly a ship rocks side-to-side when disturbed by an external force. When the waves approach the hull at comparable frequency the ship can exhibit a resonant behavior, similarly to how pushing a swing at the right time will make it swing more and more. Naval architects can affect a ship’s rolling behavior with both static and dynamic devices like [_bilge keels_](https://en.wikipedia.org/wiki/Bilge_keel) or [_antiroll tanks_](https://en.wikipedia.org/wiki/Antiroll_tanks).

# Propulsion[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#propulsion)

For the final part of this article let’s discuss how a ship manages to move forward. While sails have been a dominant form of ship propulsion for thousands of years, they can’t power a vessel if there is no wind. Modern day ships typically use [internal combustion engines](https://ciechanow.ski/internal-combustion-engine/) that power [_screw propellers_](https://en.wikipedia.org/wiki/Propeller), which look roughly like this:

The shape of a propeller may seem fairly complicated, so let’s try to devise it from first principles. A job of a propeller is to push water backwards, which, by [Newton’s third law](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion#Newton's_third_law), pushes the propeller and the ship forwards. To push the water away we’ll use a few paddle-like **blades** attached to a **hub**, all rotating on a **shaft**. We’ll start with just three **blades** placed symmetrically around the axis of rotation. Observe that we have some freedom in how we orient them:

As the propeller rotates around its axis, the forces its blades exert on water vary quite a bit depending on the blades orientation. In the demonstration below the **blue arrows** show the forces exerted on water by each blade. The sum of all these forces is shown with the **yellow arrow** and the induced swirl is depicted with the **red arrow**:

When the blades are [oriented sideways](#) they push a lot of water, but only in the **swirly** motion and the **forces** balance each other out. The engine’s work is wasted on dragging the paddles through the water. As we reduce the angle the projected area of the blades in the direction of rotation decreases and so does their pushing power. At limit it becomes negligible when the blades are [perpendicular](#) to the axis of rotation.

At [intermediate angles](#) some of the work done by the blades is still used to **swirl** the water, however, the blades also **axially push** the water away. This causes the propeller and the boat to be pushed in the opposite direction. That propeller generates _thrust_.

In this _very_ simplified analysis we seem to achieve the largest thrust roughly in the middle between the two extremes, but notice that we still have a relatively large drag induced by the blades. In practice the most efficient [_angle of attack_](https://en.wikipedia.org/wiki/Angle_of_attack) will be much lower. We can visualize it in a top down view of a single blade. For top performance the blade’s direction should stay within the **green region**:

A propeller will work most efficiently if the velocity of a blade relative to water is in that **angular range**. Let’s look at the **final velocity** of the blade a bit closer. Note that while different parts of the blade have the same [angular velocity](https://ciechanow.ski/gears/#spinning), they have different _linear_ velocity, so the moving blade approaches water with **rotation-induced velocity** which varies with the distance from the center of the propeller:

Moreover, a functional propeller will push the ship forward, causing it to sail at some speed, so the vessel and its propeller also have some **forward velocity** relative to the water:

The sum of **rotation-induced velocity** and the **“forward” velocity** creates the **final velocity** of the section on the blade. In the following demonstration, the right side shows the frontal view of the blade, making it easier to see the selected **section**:

Notice that the **area of good efficiency** is fixed against the **final velocity** of the blade. Since different parts of the blade have different velocity against water they should also have a different angle of attack so that locally they can function at maximum efficiency. To account for this the propeller blades have a characteristic twisted shape – their angle of attack _decreases_ with radial distance. In the demonstration below you can control the amount of that twist in the blades:

In its simplest form the twisted surface of a blade is a part of a [_helicoid_](https://en.wikipedia.org/wiki/Helicoid), which is a **surface** swept by a **segment** that is perpendicular to an **axis** while simultaneously rotating and moving along that **axis**:

A helicoid like the one above is defined by a **radius** which specifies the extent of the segment and a **pitch** which describes the distance travelled along the axis during a single revolution. In fact, a helicoid was also used in [Archimedes' screw](https://en.wikipedia.org/wiki/Archimedes%27_screw) which served as the base idea for first screw propellers employed in ships. With the twist in place each part of the blade stays within the **optimum range**:

The final consideration is the total blade area, which is a product of the surface of each individual blade and the number of blades. You can change the latter in the demonstration below:

Notice that in the [back view](#) a higher number of blades occupies a larger part of the entire circular shape. The bigger the total blade area the larger the thrust, but only to some extent as the flow around one blade starts to affect the flow around the other blades.

The blades of modern propellers have an [airfoil](https://en.wikipedia.org/wiki/Airfoil) cross section, which contributes to the additional lift on the blades, thus improving their efficiency. However, the pursuit of blade lift has its limitations. When the pressure on the pushing side of the blade increases it also simultaneously decreases on the other side. If that pressure reduces too much the water can locally boil, in effect known as [_cavitation_](https://en.wikipedia.org/wiki/Cavitation). When those vapor-filled bubbles repeatedly collapse on the surface of blades they can cause [significant damage](https://en.wikipedia.org/wiki/File:Cavitation_Propeller_Damage.JPG).

I need to point out that what I’ve discussed above was a simplified analysis of how screw propellers generate thrust – there are [entire books](https://www.cambridge.org/core/books/hydrodynamics-of-ship-propellers/60B96C78A2B5CC3FADC96C9512A522F6) dedicated to hydrodynamics of propellers. Propeller design is a complex topic and even minor efficiency gains can result in big savings on fuel used to power the ship’s engines.

# Further Watching and Reading[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#further-watching-and-reading)

[Casual Navigation](https://www.youtube.com/channel/UC5_HIscbiDZM0dMX-nCksuA) is a YouTube channel dedicated to maritime concepts. In his videos Rob analyzes [famous capsizings](https://www.youtube.com/watch?v=A2QfV11XYD8), discusses [antiroll techniques](https://www.youtube.com/watch?v=A2QfV11XYD8), and explains [why the bottoms of the ships are red](https://www.youtube.com/watch?v=-AdW030xQB4). The recordings strike a good balance between entertainment and education.

When it comes to books, I recommend [Applied Naval Architecture](https://www.amazon.com/Applied-Naval-Architecture-Robert-Zubaly/dp/0870334751) by Robert Zubaly. This entry level publication expands on everything I’ve discussed and touches on other topics like ship strength and [floodability](https://en.wikipedia.org/wiki/Ship_floodability).

For a different take on boats I recommend YouTube channel [Tips from a Shipwright](https://www.youtube.com/c/TipsfromaShipwrightvideos) which is dedicated to documenting the process of building and restoring smaller boats. Over the course of the last few years Louis Sauzedde has recorded his work on two full projects – a [work skiff](https://www.youtube.com/playlist?list=PLzlN3A2DLgNwE2RCpQ9vKCmeOwvKCRRjF) and a [dory](https://www.youtube.com/playlist?list=PLzlN3A2DLgNzJ5atmhj0FjWDG8sIW1Ekq). Both series show great craftsmanship and expertise. It’s a real joy to follow Lou’s progress in his workshop.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/naval-architecture/#final-words)

With experience acquired over millennia, naval architects have mastered the art of controlling the forces acting on hulls to make sure the ships, their passengers, and cargo arrive unharmed at their destination.

Both traditional and naval architects have to devise functional, safe, and habitable structures. However, naval architects face the additional challenge of designing for an ever-changing setting for their creations – the harsh and unpredictable sea.
