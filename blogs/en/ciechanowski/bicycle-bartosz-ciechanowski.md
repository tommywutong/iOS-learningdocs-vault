---
title: Bicycle – Bartosz Ciechanowski
source: Bartosz Ciechanowski
source_key: ciechanowski
source_url: 'https://ciechanow.ski/bicycle/'
original_language: en
published: ''
status: active
license: Copyright © Bartosz Ciechanowski（页脚）→ 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:4c1133a80a439d57'
translated: false
---

> 原文：[Bicycle – Bartosz Ciechanowski](https://ciechanow.ski/bicycle/)　·　Bartosz Ciechanowski

# [Bicycle](https://ciechanow.ski/bicycle/)

There is something delightful about riding a bicycle. Once mastered, the simple action of pedaling to move forward and turning the handlebars to steer makes bike riding an effortless activity. In the demonstration below, you can guide the rider with the **slider**, and you can also drag the view around to change the camera angle:

Compared to [internal combustion engines](https://ciechanow.ski/internal-combustion-engine/) or [mechanical watches](https://ciechanow.ski/mechanical-watch/), bicycles are fairly simple machines – most of their parts operate in plain sight. What’s not directly visible are all the forces that make it possible to ride and control a bicycle without compromising the structural integrity of its components.

In this article, I’ll focus on the delicate interplay between many of the forces that act on a bicycle and its parts when riding. We’ll witness how forces applied through tires make a bicycle accelerate, brake, and turn, and we’ll also investigate how the wheels and the frame handle those different forces without breaking.

Before we understand these more complicated interactions, we’ll play with much simpler objects. The basic scenarios we’re about to explore will help us develop an intuition about the behavior of a real bicycle.

# Forces[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#forces)

Let’s introduce the unassuming protagonist of this section – a plain wooden box. In the demonstration below, you can use the slider to apply a **force** to this box. The little speedometer in the bottom part tracks the velocity of the crate. You can restart the simulation using the  button:

The **red arrow** represents the pushing force, which could be applied by a hand, or a strong gust of air. The size of that **arrow** reflects the magnitude of that force – the bigger the arrow, the stronger the pushing action.

Notice that once the block is moving, it will continue to move with the same velocity even when you stop applying the **force**. In the magical world of these simulations I removed all friction or air resistance – the only forces present are the ones we see.

As you apply that **force** on the block, it increases its velocity – the bigger the force, the faster the acceleration. Moreover, for the same force, the bigger the mass of the box, the _slower_ it will accelerate. You can experience this in the demonstration below, where the bigger box is twice as heavy as the smaller box, but the **applied forces** are the same:

While in this article I’ll mostly avoid the underlying mathematical details, the relation tying the applied force **F**, the mass of the object **m**, and the output acceleration **a** of that object, deserves to be presented in one of the most fundamental equations in physics:

F = m · a

Let’s complicate things a little by adding a **second force** that is trying to push the box to the left. You can still control the magnitude of the **right-pushing force** with the slider, but to make our experiments a little easier, I’ll restore that **force** to its original magnitude after you let go:

Notice, that it’s not the mere presence of forces that causes an object to accelerate – the velocity changes only when these forces are not _balanced_. Recall that we’re representing the magnitude of forces using arrows of different sizes, so as long as the length of the **right-pointing arrow** is equal to the length of the **left-pointing arrow**, the box won’t change its velocity.

It’s worth pointing out once more that when the box starts to move due to force imbalance, just letting the slider go to balance the **two** **forces** again will _not_ stop the box – it will keep moving with some velocity. To slow the crate, we need to change the balance of forces to work _against_ the current motion, and do it carefully enough to avoid overshooting.

Let’s explore one more concept related to these simple forces. In the demonstration below, the box is resting against a **wall** and you can once more control the **force** pushing that box to the right:

Similarly to the previous examples, as we **apply a force** on the box we’d expect it to move, but it doesn’t budge at all, which implies that there must be some other force acting on it to balance that **pushing force**. Let’s visualize all the other forces present in this scenario:

Notice that as we **push** the box, that box **pushes** on the wall, but the wall **pushes** the box back, and it’s _that_ **force** that balances the **pushing force**, which keeps the box static. Let’s draw the box and the wall separately to show the forces acting on each one:

The wall is firmly attached to the ground, so the **force pushing** on the wall is effectively trying to push the entire Earth. Since our planet is _very_ heavy, the acceleration of the Earth and the wall attached to it is effectively non-existent.

You may wonder how the wall knows how much back-force to apply, so let’s look at the interaction between these two objects up close and in slow motion. As we apply the **force**, the box actually starts accelerating into to the wall, pushing its surface to the right:

As the box moves to the right, it compresses the molecules in the wall, which create a spring-like **force** that pushes the box back. If that **force** is too small to balance the **pushing force**, the box will continue to move to the right, which compresses the wall even more, creating an even larger **push-back force**.

If that **force** grows too large and overpowers the **pushing force**, it will start to accelerate the box to the left, which will slow it down and even move it back to the left. This will then reduce the compression of the wall, which in turn decreases that **resisting force**. The entire system very quickly finds its balance, and since the wall and box are very stiff, the final displacement isn’t perceptible.

In this next demonstration we’re complicating things a little by applying an inclined **force** that’s pushing the box into the corner:

As the box is not moving, the forces acting on it must be balanced, which we can see in the right side, where I’ve tallied up head-to-tail all the arrows representing the forces acting on the box to show that they form a closed loop. We can also decompose the angled **pushing force** into its **horizontal** and **vertical** components – these are balanced by the **horizontal** and **vertical** reaction forces from the wall.

Before we finish up with these simple forces, let’s explore what happens when we line up two boxes next to each other and try to **push** the left one towards the wall:

As we **push** the first box, it **pushes** on the second box, which then **pushes** on the wall. Notice that the wall doesn’t know that there are two boxes there, it just feels the effects of that single **pushing force**. The wall **pushes back** on that second box, which in turn **pushes** on the first box. To make things clearer, we could even separate the boxes and draw forces acting on each one, showing that both crates are in balance:

Although I’ve shown them explicitly here, there is nothing special about the **two** **forces** _between_ the boxes. Equivalently, we could draw forces between every plank of wood in these crates – each plank pushes on its neighbor and is also pushed back by it. If we were to look closely enough, we could draw the arrows between the individual molecules constituting these boxes – they’re all steadily kept in balance by the surrounding forces exerted by the neighboring particles.

In this article, I’ll sometimes visualize these _internal_ forces, as they will help us understand the behavior of individual bicycle components, but note that it’s up to us to decide where we want to draw these artificial separating boundaries to expose the internal reactions.

The ideas we’ve explored in this section are collectively known as [_Newton’s laws of motion_](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion), and they are fundamental for understanding how objects move and interact with each other when forces are applied. However, there is a little more we need to explore to understand the behavior of a bicycle.

# Moments[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#moments)

You may have realized that the forces we’ve been applying to the boxes have been conspicuously pointing at the centers of those objects. Let’s see what happens to this box when we exert a **force** that isn’t so neatly aligned:

As you can see, the box still moves to the right, but it also starts to rotate and continues to rotate after the force disappears. Notice that I marked the box with a small black and white symbol  that symbolizes the [_center of mass_](https://en.wikipedia.org/wiki/Center_of_mass) of this object.

I’m also drawing a dashed line through which the force operates. In this example, the line doesn’t go through the box’s center of mass, but it’s placed at a distance from that center. This creates a lever arm through which the **force** rotates the object.

The further away that line is from the center of mass, the easier it is for the force to rotate the object. In the following demonstration, you can apply **two forces** of the same magnitude to two identical boxes. The only difference is the **distance** to the center of mass  at which these forces act:

When the **distance** between the force-line and the center of mass is large, the box spins faster as well. That distance doesn’t change the acceleration of the box to the right and both boxes move with the same _linear_ speed. However, that **distance** affects the _angular_ acceleration of a box – the longer that **arm**, the faster the box spins.

The product of the force **F** and the length **r** of the arm at which it acts is known as _moment of force_ or [_torque_](https://en.wikipedia.org/wiki/Torque), which we can represent with a letter **M**:

M = r × F

While in three dimensions the moment of force can rotate an object around an arbitrary axis, in these simple two dimensional scenarios we just care if torque rotates the object clockwise or counterclockwise.

Naturally, every off-center force applied to an object creates torque. In the demonstration below you can shift the position of **two** **forces** acting on the block:

The _forces_ remain balanced and the object’s center of mass stays in place, but the _moments_ of forces are not balanced and the object changes its angular velocity.

While it’s harder to visualize the balance of moments, we can still do it by drawing colored rectangles spanning the length of the acting force arrow and the force arm:

The **red force** wants to rotate the box in the counterclockwise direction. The **blue force** wants to rotate the box clockwise and that force is twice as large as the **red force**, but it also operates at half the distance. The resulting **red** and **blue** areas are the same, which indicates that the moments are balanced. The **green force** goes through the center of mass so it doesn’t rotate the crate, it just balances the other **two** **forces** to prevent the box from moving to the right.

Before we put the boxes back in a warehouse, let’s take a final look at one more trick we’re going to use to make it easier to visualize forces. In the simulation below, I added Earth-like gravity that attracts the cube to the bottom of your screen. Both left and right view show the same cube and the same **gravity** and **ground reaction forces** acting on that cube – they’re just visualized differently:

When put in this gravitational field, every individual molecule of that cube is being pulled down to the bottom, and once the cube lands, every molecule of the ground under that cube pushes back on it – you can see that roughly presented on the left side.

While more realistic, that soup of arrows is a little messy and hides the simpler, but equally valid notion of **gravity** and a **ground reaction force** acting on that cube – you can see them on the right side.

If we tally up all the small ground forces and moments they create we can replace them with a **single arrow** centered at the bottom of the cube. For gravity forces we can replace them all with a **force** located at the _center of gravity_, which for most purposes is equivalent to the location of the center of mass .

The rules we’ve explored here are universal – unbalanced forces change linear velocity of an object, and unbalanced moments change _angular_ velocity of an object. We’re finally ready to understand how these ideas apply to a bicycle and a rider. Let’s draw _some_ of the forces that act on them during a steady turn:

As you can see, it’s easy to get overwhelmed with all the arrows pointing in different directions. We’ll eventually understand all of these forces, but we’d preferably start with a more welcoming approach.

Instead of analyzing all the complex 3D interactions in a single shot, we’ll first look at simpler situations that can be easily presented in flat diagrams. We’ll also decompose the motion of the bike and rider into three primary directions, and only then will we see how they interact with each other.

In fact, we’ll begin by exploring the direction in which there’s commonly no movement at all – the vertical one.

# Up and Down[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#up-and-down)

Let’s look at a diagram of vertical forces acting on a bicycle and its rider that are coasting down a road. A chunk of the **rider’s weight** rests on the seat, which **pushes** it back, but the pedals and the handlebars **support** some of that **weight** too. The **weight** of the rider _and_ the bike is then **carried** by the ground through the two contact points under the wheels:

As you’ve probably realized, the **yellow slider** allows you to change the posture of the rider. Notice, that the **reaction** **forces** from the ground shift back and forth when this happens.

It may appear that the ground is aware of the rider and the **weight** of his torso and limbs, but note that the ground only feels the **two** **forces** exerted by the wheels. Although that load could be slightly different during the _dynamic_ part of the rider’s leaning, once settled, these **two** **forces** perfectly sum up to the combined weight of the bike and the rider, keeping them in balance. After all, the bike and the rider neither fly away nor sink into the ground.

To understand why these **ground** **forces** change their distribution as the rider leans, we first have to visualize the center of mass of the bike , the center of mass of the rider , and the center of mass of _both_ bike and rider . The rider is many times heavier than the bike, so it dominates that shared center of mass :

As the rider leans forwards or backwards, the position of his center of mass  changes, which in turn shifts the center of mass of the combined system . This causes the moments of forces to no longer be balanced, and the bicycle and the rider start to rotate around their center of mass. Let’s see this in a _vastly exaggerated_ form in the demonstration below where the slider controls the time progress of this event:

When the rider’s position shifts, the arm lengths for the reaction of the ground also change, which creates a net torque that rotates the bicycle counter-clockwise. In practice, the actual rotation is very tiny, but as it happens, one of the wheels lifts a little, which decreases the **ground reaction force** in that area. Simultaneously, the other wheel bites into the ground a little more, which _increases_ the **reaction force** under that wheel.

It may once again feel a bit magical that the ground somehow knows how much force to distribute to each wheel, but this behavior follows from a careful balance of the ground’s springiness, very similar to the one we’ve seen with a wall resisting a box pushing on it. In the demonstration below, you can once more **change** the rider’s position, but this time we’re watching the contact areas between the **tires** and the **road** from up close and in slow motion:

The entire system very quickly finds the right balance that equalizes the two torques and the **ground** **forces** also keep ensuring the equilibrium in the vertical direction – they add up to counteract the **weight of the bike and rider**.

So far we’ve completely ignored any forces in the forwards and backwards direction, which allowed the rider to coast forever without any pedaling. Naturally, this was a simplifying assumption, and during a typical ride on a flat ground the rider has to pedal to keep moving forward:

On their own, these dynamic forces exerted by the rider’s legs barely affect anything about the distribution of the ground reaction forces – one can’t make oneself heavier by just pressing harder on the ground.

However, through the cranks, chain, and the rear wheel, that pedaling creates a force that pushes the bicycle forward. As we’ll see, these horizontal forces can also affect _vertical_ balance, but let’s first understand how the pedaling action propels the bicycle.

# Forwards and Backwards[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#forwards-and-backwards)

Let’s start by looking at what happens to various bike components as the rider **presses** a pedal:

The **pedal-pressing force** generates a **torque** that acts on the front sprocket, which is studded with teeth. That sprocket then **pulls** on the chain, which then **pulls** on the rear sprocket generating a **torque** on the rear wheel. That rear wheel **torque** can then apply a **force** that will try to push the ground back.

Notice that the forces and moments change their magnitude as they pass through each component. That transformation is the consequence of different radii and lever arms involved in the pedaling process. For example, the cranking action forms a simple lever:

The crank serves as the **input lever**, and since the **crank’s length** is larger than the **radius of the sprocket**, the **output force** is also larger than the **input force**. Since the sprocket is rigid, every point on its circumference can exert this force, so the chain is also **pulled equally strongly**.

The chain then pulls on the rear sprocket, which has a different **radius** than the **front** one. As a result the **chain force** also acts on a different arm length:

The rear sprocket is smaller on our bike, so the **torque on the rear wheel** created by the **pulling chain** is smaller than the **torque on the front wheel**, but more complicated bicycles allow the rider to change the [gearing ratio](https://ciechanow.ski/gears/) – this can magnify or minify the rider’s **pedaling torque**.

Through the friction between the tire and the road, the bottom part of the wheel stays in contact with the ground, so that as the wheel rotates, it **pushes** the ground to the left. As a reaction to that **force**, the ground **pushes back** on the wheel to the right, which pushes the bike and the rider forwards:

The little speedometer in the top left corner shows the current speed. I’m using imperialmetric units here, but you can [switch](#) to the metricthe imperial system if you prefer.

Although **these** **forces** apply in a different direction than the weight-related forces we’ve looked at before, they’re yet another manifestation of the principle of action and reaction. The **force** that the wheel exerts tries to push the Earth back, but its mass is enormous, so the planet’s acceleration is microscopic, but the **force** of the same magnitude applied to the bike easily speeds it up.

Notice that the **pressing** **forces** generated by the rider vary across a single rotation. Moreover, the arm length at which these forces act also changes during each cycle, so the final torque and the outcome **pushing force** generated by the rider also has a periodic nature.

Looking at the little speedometer you may have noticed that the bike stays at roughly the same speed, even though it’s being pushed forward by the pedaling action. There are other forces slowing it down, which prevent more velocity from building up, but before we see those forces we should talk about a more direct way to slow down a bicycle.

A force that pushes forwards on a wheel accelerates the bicycle and its rider, and, similarly, a force that pushes backwards on a wheel will decelerate the bicycle. This idea underlies how braking works:

As the rider **pulls** on the brake lever, that lever **pulls** with mechanical advantage on the cable. The cable then **pulls** on one of the caliper arms of the brake, causing them to close, which **presses** the brake pads against the wheel.

When a wheel is spinning, that **pressing force** resists the rotational motion of the wheel by applying a friction force acting in the direction _opposite_ to the wheel’s rotation.

Let’s experience this in the demonstration below. When the rider **pulls** on the brake, the brake pads create **friction**, which creates a torque that slows the wheel and the tire down. Through friction with the road, the tire introduces a **force** that tries to push the ground forward, and the ground responds by **pushing** the tire and the entire bicycle back:

Clearly, both acceleration and braking requires some interaction between the tires and the ground. Let’s look at the details of how a tire actually generates these forces.

A typical bicycle tire has a donut-like [_toroidal_](https://en.wikipedia.org/wiki/Toroid) shape and is pressurized, but it still flattens a little when **loaded** with weight of the bike and rider, so the area where it touches the road has a roughly elliptical shape. You can see that shape on the right side of the following demonstration, in the zoomed-in view of the **small section** of the road on which the tire is resting:

This region is known as the [_contact patch_](https://en.wikipedia.org/wiki/Contact_patch). It may seem obvious once pointed out, but the two elliptical regions under the two tires are the only places where the bicycle interacts with the road and _almost all_ of the rider-controlled forces have to act through them.

To understand how forces in the contact patch get developed during acceleration and braking, we have to first look at a rolling motion. In the demonstration below, you can play with a lone wheel rolling down the road. The wheel is covered in white paint, so it leaves marks on the ground. The sliders let you control two different types of velocity. The first one controls the forward motion or the **linear velocity**, and the second one controls the rotational motion or the **angular velocity**:

You may have noticed that in [some positions](#) the wheel looks like it’s mostly sliding, in [others](#) it looks like it’s mostly spinning. These two situations may look a little unusual, but you’ve probably seen a vehicle’s wheels sliding when braking, or spinning when accelerating too quickly. When we keep the two velocities at the [right](#) [proportions](#), the wheel looks like it’s rolling smoothly, and the paint marks it leaves are more or less as long as the ones on the tire.

When the wheel rotates “just right”, its angular velocity denoted with a Greek letter omega **ω**, is tied to its linear velocity **v** with a simple equation involving the _effective_ radius **r** of that wheel, which is slightly smaller than the outer radius of the tire as it compresses a little under load:

ω =  v / r

Since a wheel is attached to a bicycle, the forward linear velocity **v** of the wheel is always equal to the velocity of that bike. When the external forces are balanced and the bicycle rolls freely, the angular velocity **ω** of the wheels will be equal to the natural, free-rolling angular velocity for that speed **v**.

In the demonstration below, you can experience what happens in the contact patch area during those free-rolling conditions. I put little markers on the **inner** and **outer** parts of the tire to show their relative movement. The slider lets you scrub back and forth in time:

In this free-rolling scenario, the **inner** and **outer** parts of the tire stay in sync as the wheel smoothly rolls over the road.

Things change a little when the rider starts to pedal. Recall that the torque that the chain exerts on the rear sprocket makes that rear wheel rotate faster – the angular velocity of that wheel increases a little, but the forward velocity stays the same, as the bike itself hasn’t yet accelerated.

In the demonstration below, you can see what happens between the road and the tire, when the wheel has a slightly increased angular velocity:

As this wheel rotates, the high friction between the road surface and the rubber causes the **outer** part of the tire to stick to the ground, while the **inner** part of the tire continues to turn with the wheel. Since the wheel rotates a little faster than its free-rolling speed, it pulls the **inner** parts away from the stuck **outer** sections.

This causes the tire to deform near the contact patch area. It’s _that_ deformation that makes the tire want to push the ground back – you can almost see it trying to sweep the road to the left. The ground reacts by pushing the tire and the entire bike forward.

This force is created because of the difference between the free-rolling angular velocity of the wheel and the _actual_ angular velocity of the wheel – the latter has been increased by the pedaling action. The generated pushing force accelerates the bike, which increases the natural free-rolling speed of the wheel until it matches the actual speed of the wheel, at which point the deformation will no longer be present and no additional forces will be created.

Similarly, as the rider presses the brakes, causing the wheel to rotate slower than its free-rolling speed, the **inner side** of the tire also starts to shift relative to the **outer side** that sticks to the ground. This deforms the tire in the opposite direction:

This deformation creates a force pushing the bike backwards, which slows it down, which then reduces the free-rolling speed of its wheel.

Unfortunately, there are limits to the deformation a tire can handle without locally loosing contact with the ground and starting to skid – you may have noticed these limits in the rear part of the tire, where the **outer** sections eventually break away from the road and start sliding.

Let’s explore the magnitude of forces that a tire applies a little closer. Intuitively, the more deformed the tire, the bigger the forces it exerts. That deformation, and thus the developed forces, depends on the difference between the actual angular velocity of the wheel **ω** and its free-rolling angular velocity **ω~0** joined in the parameter **s** known as the [_slip ratio_](https://en.wikipedia.org/wiki/Slip_ratio):

s =  ω − ω~0 / ω~0  =  ω − v/r / v/r

Let’s explore these dependencies in practice. In the demonstration below, the free-rolling angular velocity **ω~0** depends on the **forward speed** **v** of the wheel. Just like before, you can tweak the **actual angular velocity** of the wheel **ω** with the second slider:

When the wheel **rotates** at the [free-rolling speed](#) of the current **velocity**, the slip ratio is 0. When the wheel [rotates _faster_](#) than the free-rolling speed, which happens when we pedal, the slip ratio is positive. Finally, during braking, when the wheel [rotates slower](#) than the free-rolling speed the slip ratio is negative. When [starting](#), the _theoretical_ slip ratio may become infinite, but in practice, as the rear wheel starts turning, the force developed by the tire immediately starts pushing the bicycle forward.

Other than the slip ratio, the magnitude of forces a tire can exert depends on road conditions, speed, tire pressure and wear, and, most importantly, the **vertical load** on that tire. The plot below roughly demonstrates that dependence of the output force on the slip ratio, and the **vertical load**, which you can control with the slider:

When the wheel rotates faster than the free-rolling speed and the slip ratio is positive, the generated force is positive and it **pushes the bicycle forward**. While initially that force grows proportionally to the slip ratio, it quickly reaches a maximum and tapers out.

Similarly, when the rider brakes, the wheel rotates slower than the free-rolling speed and the slip ratio is negative, the output force is negative, as it **pushes the bicycle backward**. It’s worth pointing out that a tire generates the largest braking force for smaller values of slip – braking is actually less efficient when a wheel completely locks up and slides over the road.

Let me also point out that the forces generated by the tire against the ground affect the wheel itself. For example, when the wheel rotates slower than the free-rolling velocity, the forces that the tire generates are not only slowing the bike down, but they also want to accelerate the wheel. Ultimately, this is how a front wheel starts to rotate as the bike starts moving, even though it’s only the rear wheel that’s powered.

The larger the vertical load on the wheel, the bigger the braking or accelerating forces. We’ve already seen how the position of the rider can affect the vertical loads on the wheels, but those vertical forces are also affected by the braking and accelerating forces themselves. The latter are typically much smaller, so let’s focus on braking.

In the demonstration below, the slider controls the **force** applied by the rider on the rear brake lever. As the brake pads start rubbing against the rotating wheel, they create **friction**, which makes that rear wheel rotate slower. As a result, the rear tire introduces **braking forces**. The speedometer in the top left corner shows the current velocity of the bike:

Notice that the **backward force** applied at the rear wheel not only slows the bike down, but it also wants to rotate the bike and rider clockwise around their center of mass . Similar to our previous examples, the ground reaction forces adjust by increasing the **load on the front wheel** and decreasing **the load on the rear wheel** to compensate for this additional torque.

At some point, that **braking force** reaches its maximum value. Recall that the forces generated by a tire depend on the vertical load, so any further increase in that **braking force** would unload the **rear wheel** more, which then would _decrease_ the tire-generated **braking force**. Additionally, the rear wheel can lock up quite easily, as the **clamping friction** can get much stronger than the relatively weak **braking force** that tries to keep that wheel rotating.

As we’ve just seen, the rear wheel can only apply a limited amount of braking force, so let’s explore what happens when we brake with just the front brake instead:

The **braking force** also wants to rotate the bicycle clockwise, which increases the **load on the front wheel**, which then _increases_ the **braking force**, because a loaded tire generates more force. Notice that by braking with the front brake we can halt to a stop much faster, but there is a certain risk involved with applying _too_ much of the front-braking force.

As that **braking force** grows larger, it unloads the **rear wheel** more and more. At some point it can even cause the rear wheel to get completely unloaded, and the **braking force** will eagerly try to rotate the bike and rider further:

Since the center of mass is relatively high, the torque induced by the **braking force** overpowers the torque from the **front wheel reaction** and the bicycle starts to rotate, but simultaneously that **ground reaction force** lifts the bicycle and the rider.

Naturally, braking forces are not the only ones that slow a bicycle down. At typical speeds the primary resistance to perpetual motion comes from the **air drag**, which is proportional to the _square_ of the velocity, but it also depends on the shape and size of the rider and the bike facing the incoming air – professional cyclists will often change their position when riding downhill to [minimize drag](https://www.sciencedirect.com/science/article/pii/S0167610518305762).

In the demonstration below, you can control the **cadence and strength** of the rider’s pedaling using the slider to see how the **air drag** rises as the rider gains speed:

Although the **aerodynamic resistance** pushes on every front-facing part of the bike and the rider, we can aggregate these effects into a single force acting on the [_center of pressure_](https://en.wikipedia.org/wiki/Center_of_pressure_(fluid_mechanics)), which I’m visualizing it with a **blue dot**.

While [more energetic](#) pedaling accelerates the bicycle, that effort is quickly countered by the increased **air drag** caused by increased speed. A bicycle also gets slowed down by the rolling resistance of the tires and other frictional losses in the rotating parts. To keep a steady forward speed, a cyclist has to keep pedaling to provide a **pushing force** that counteracts these regressive forces.

Recall that with the same force, a heavier object accelerates slower, so the reduction of the weight of the bicycle is important for improving its responsiveness to more intense pedaling or braking. Low weight is even more vital when riding uphill:

Recall from our wooden box playground that we can always decompose an angled force into more convenient directions. The force of gravity still acts straight down, and the vast majority of it pushes the bike and rider perpendicularly into the tilted ground, but a small component of that gravity is parallel to the road and it **pulls them downhill**. The lighter the bike and rider, the smaller that force and the easier it is to keep riding uphill.

Throughout all these examples we’ve witnessed how the two ground forces underneath the wheels redistribute themselves as the rider changes position, or when aerodynamic and braking forces slow the bicycle down. It was only in the quite extreme front-braking conditions when the bicycle lost its front-to-back balance and flipped over.

Unfortunately, if we look at a bicycle from behind, the situation gets drastically different. Let’s explore how different forces affect the side-to-side behavior of a bicycle.

# Left and Right[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#left-and-right)

In the demonstration below, you can witness what happens to the bicycle and its inattentive rider who is holding the handlebars in the straight-ahead direction, as they together tilt away from the vertical even by a small amount. By dragging the slider, you can directly control that **leaning angle**, but once you let go, the forces will take over:

The intuitive way to understand why this happens is to notice that the **friction** between the tires and the ground makes the contact patches act like hinges on which the bicycle can pivot. As the **gravity** develops an arm against that pivot, it rotates the bicycle more and more until it eventually falls down.

Notice that the fall is self-perpetuating – as soon as the **gravity** develops an arm force, the bike will lean even further, which increases that arm and the rotating moment. In the front-to-back direction, the two wheels provided two points of support that could trade the load to keep the bike balanced. In the side-to-side direction, the contact patch under a tire is very narrow and it can’t provide much support, which makes the entire system very easy to tip over.

While this situation often happens when learning to ride a bike, most riders have very little trouble keeping a bicycle upright. One could assume that riders simply balance their bodies left and right to keep the center of mass over the tires to minimize the force arm of **gravity**. After all, a skilled cyclist can easily ride a bike hands-free using only the body motions to keep the bicycle straight.

Unfortunately, merely tilting the body to change the position of the center of mass is often not enough, which you may have experienced trying to balance yourself on a bicycle that’s _not moving_ and has its brakes locked to prevent any subtle forwards or backwards motions. In the simplified simulation below, you can try to balance such a stationary bicycle by **tilting the rider’s body** with the slider. Be ready for action as soon as you start over with  button:

Despite the labored contortions of the rider, the center of mass doesn’t move that much, making it very difficult to balance a bicycle this way. Before we solve the puzzle of hands-free stability in motion, let’s explore a more typical way of keeping the bike upright when riding by simply gently turning the handlebars.

In the demonstration below, you can witness what happens to the bike and rider as the handlebars are turned. I keep the camera directly behind the bike so that you can see how it tilts away from the vertical. The slider controls the progress of time:

Unfortunately, we’ve reached the limits of what we can easily visualize using these flat illustrations. Even though we leave the green pastures behind and enter the kingdom of infinite checkerboard pavement, we at least make it easier to show these forces from different angles. The demonstration below shows the exact same situation as the one we’ve just seen:

When the handlebars are turned and the front wheel doesn’t point straight at the direction of travel, the front tire generates a **side force**. The rear tire follows very quickly, and **both forces** start to counter the tilt of the bicycle, which straightens it up. The indicator in the bottom right corner shows the current steering angle of the front wheel.

Notice that instead of trying to shift the center of mass on top of the contact patches of the tires, this gentle steering action pushes these contact patches _under_ the center of mass – this also reduces the arm length of **gravity** to zero.

In general, as the bicycle starts to tilt to a side, the rider can gently steer into that leaning side, which develops a force that restores the bike and rider to the vertical. As the bike straightens, the rider also repositions the handlebars.

Naturally, even if the bike gets back to a perfectly balanced position, it will quickly get disturbed away from it, so during a normal ride the correction process happens continuously as the rider subconsciously reacts to the changes in the tilt of the bike and his body.

The development of this side force may seem a little mysterious, so let’s take a closer look at what happens between the tire and the ground after the rider turns the handlebars. Firstly, notice that it’s possible for a wheel to be **traveling at** a slightly different direction than it’s currently **aiming at**:

The angle spanned between these two directions is known as the [_slip angle_](https://en.wikipedia.org/wiki/Slip_angle). As you may suspect, a non-zero slip angle is a little unnatural for a tire, so it will undergo some deformation when forced to roll like this.

In the demonstration below, I put a bunch of small points  on the circumference of the tire, I also made that tire semitransparent to make it easier to see what’s going on in the contact patch area:

Recall that the contact patch has a shape of a long ellipse. When a tire rolls with a non-zero **slip angle**, the first point of contact with the ground happens to the side of the central axis, that I’m showing with a **thin blue line**. Due to friction, the tire sticks to the ground in that area, so that part of the tire doesn’t follow the motion of the wheel and is gets **deformed away** as the wheel rolls forward.

This **deformation** generates a **force** that wants to push the wheel to a side to minimize that **deformation**. Eventually, these deforming forces become large enough to overcome the friction, and the rear section of the tire slides across the ground.

I need to note that when you change the **slip angle** in the demonstration, I’m showing you the deformation of the tire in its fully developed state for that angle. In the physical world it can take a [small amount of travel](https://en.wikipedia.org/wiki/Relaxation_length) for the tire to deform and exert full force.

As we may expect, the magnitude of the side force depends on the slip angle, but similarly to the forward and backward forces developed by the accelerating and braking tires, the side forces developed by a tire are also strongly related to the **vertical load** on the wheel:

Naturally, the bigger the slip angle, the bigger the deformation and the resulting force in **one direction** or **the other**, but at some point the tire gets too deformed and it will start mostly sliding, which limits the side forces it can generate.

There are two other aspects of tire behavior that are worth mentioning. Firstly, a tire can only sustain a certain amount of deformation in _any_ direction without breaking contact with the ground, so it’s much easier to start skidding when braking _and_ turning at the same time. Secondly, a leaning tire pointed in the direction of travel can still generate some side forces through an effect known as [_camber thrust_](https://en.wikipedia.org/wiki/Camber_thrust), but it’s usually a few times smaller than the regular slip angle forces, at least at typical angles of side tilt.

While vital for stability, the side force generated by tires also allow a bicycle to turn. In the demonstration below, you can witness a bicycle and a rider in a steady turn:

Looking at this situation [from behind](#), we can see that the **side tire forces** try to restore the bicycle to the vertical position by rotating clockwise around the center of mass . The moment **these forces** generate helps to balance the **reaction forces** trying to tilt the bicycle towards the ground. Although this bicycle is not vertical, it doesn’t lean any further because the moments are balanced – this explains why the bike and rider tilt during a turn.

If we look at this situation [from above](#), we can also notice that the **forces** generated by the tires push the bicycle to the left. Since **these forces** are tied to the bicycle, they continuously keep changing their direction, which makes the bicycle move in a circle.

Throughout these examples you may have found it a little surprising that both tires generate a side force. That behavior is a consequence of a circular motion. In the demonstration below, you can witness that during a steady cornering, the current velocity of the **front wheel** and of the **rear wheel** is tangent to the circle that the rider is taking:

To straighten a bicycle that’s turning left, the rider has to turn left even more, which will increase the slip angles and the forces that the tires generate. This is the exact same behavior that happens when the rider tries to remain stable:

Finally, let’s explore how a rider _enters_ a turn. One could assume that to start turning left from a vertical position, the rider also has to turn the handlebars to the left. In the demonstration below, you can see what happens in that scenario:

Notice that tires generate forces that lean the bicycle to the right. However, to turn left we need to lean to the left as well. To engage a left lean from a straight position, the rider must turn the handlebars to the right, and then, once the bicycle starts tilting to the left, the handlebars can be turned left:

This may sound quite surprising, but this is exactly how a bicycle turns! This initial countersteer in the opposite direction is usually something that a rider does subconsciously. However, this explains why it’s so uncomfortable to ride close to a curb, because getting away from the curb first requires getting a little closer to it. It’s all very unintuitive, but some [special bicycles show](https://www.youtube.com/watch?v=9cNmUNHSBac&vl=en) that it’s impossible to turn when we prevent that countersteer.

This whole discussion brings us a step closer to understanding how a skilled rider can control a bicycle _without_ touching the handlebars. In fact, we’ll go one step further by looking into what causes many bicycles to [remain stable without a rider](https://www.youtube.com/watch?v=j0ilP8kb8dM), at least in a certain range of speeds.

# Stability[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#stability)

The self-stabilizing behavior of bicycles has fascinated researches for over hundred years, and over time, two explanations became popular, but as we’ll see, the stability story is a bit more complicated.

It is sometimes believed that what gives a _moving_ bicycle its stability is the rotation of its wheels that could be causing some sort of gyroscope-related stabilization that prevents a bicycle from tilting to the sides, similarly to how a spinning top can maintain its balance without falling.

While it’s true that rotation of the wheels helps, this stabilizing effect is a little more subtle. In the demonstration below, a **red string** is tied to the handlebars to prevent the front wheel from steering. By dragging the slider you can see what happens to this bicycle after it is brought up to speed and let go:

The bicycle still very easily falls to the side despite the rotational motion of its wheels. For a bicycle it’s not the mere _presence_ of spinning wheels that helps with balance, but it’s the way a spinning object behaves when forced to rotate around some other axis. These effects are quite unintuitive so let’s briefly run two experiments.

In the demonstration below, you can see a stationary bicycle wheel visualized with its **three** **major** **axes**. By using the slider you can apply a torque that rotates the wheel around the **green axis**:

This follows what we’ve learned about torques creating angular acceleration, which then makes the wheel rotate faster and faster.

In this next demonstration, the wheel is spinning around the **red axis**, and you can also apply a torque that rotates the wheel around the **green axis**:

Unexpectedly, the wheel ends up rotating around the **blue axis**! These three dimensional rotational motions of already spinning bodies are a bit [more complicated](https://www.youtube.com/watch?v=ty9QSiVC2g0&t=55s) than what we’ve seen so far, but for our use it suffices to say that this [_gyroscopic effect_](https://en.wikipedia.org/wiki/Gyroscope) couples the three axes of rotation together.

While that scenario may have seem a little abstract, the exact same situation happens in a moving bicycle as it leans. The front wheel spins around the **red axis**, the tilting induces rotation around the **green axis**, and the gyroscopic effect wants to rotate that front wheel and the entire front assembly around the **blue axis** _into_ the turn:

Naturally, the construction of the bicycle prevents the front from rotating _exactly_ around the **blue axis**, but it can freely rotate around the steering axis. As the front wheel steers into the turn, the bike’s tires develop side forces, which straighten the bicycle up, similar to how it works when a rider does the steering.

Given what we’ve experimented with, one could assume that it’s the gyroscopic effect that’s responsible for stability, but it’s possible to construct special bicycles that remove the gyroscopic effect by adding an [additional wheel](http://www3.eng.cam.ac.uk/~hemh1/gyrobike2.jpg) that rotates in the opposite direction. A bicycle like this is still somewhat rideable without hands, so there must be some other factors contributing to stability.

Let’s take a closer look at the geometry of the bicycle from a side. If we draw a dashed line extending from the steering axis all the way to where  it intersects the ground we can notice that the place  where the front wheel touches the ground is _behind_ that point :

This **distance** is known as [_trail_](https://en.wikipedia.org/wiki/Bicycle_and_motorcycle_geometry#Trail) and it depends on the geometry of the front part of the bike – the **steering axis angle** and the **fork offset**. Notice that some combination of these parameters would require a more invasive redesign of the bicycle frame to make the front wheel fit.

When a bicycle is falling to a side, an upwards-pointing ground reaction and sideways-pointing friction form **combined reaction forces** that are not pointing at the bike’s center, but they’re tilted at a small angle to the bicycle:

Let’s take a closer look at the **reaction force** acting on the front wheel. In the demonstration below, you can track its direction as the bicycle leans to a side:

Notice that we can decompose this **force** into the component acting **in the plane** of the wheel and into the component acting **perpendicular to the plane** of the wheel. It’s that **perpendicular component** that acts at a trail-related arm relative to the **steering axis**, causing the front wheel to steer.

Similarly to the gyroscopic effect, this trail effect makes the front wheel steer into the fall, which creates tire side forces that straighten the bicycle up. This may all sound convincing, but notice that once the tire develops a **side force**, the trail also acts as an arm that helps to _straighten_ a turned wheel:

For typical bicycles gyroscopic and trail effects are important, but one can’t explain the influence of these actions with individual examples – both effects form a dynamic system that evolves as the bicycle leans to a side. Moreover, it’s possible to create [very unique bicycles](https://www.youtube.com/watch?v=YdtE3aIUhbU) that are self-stable without gyroscopic effects _and_ without any trail.

Bicycle stability can’t be explained using just one or two mechanisms. It’s a combination of many different intertwined factors, like the mass distribution of individual components, size of the tires, geometry of the frame, and others.

For hands-free riding, the rider can tilt his body to gently change the position of the center of mass, which then induces a lean to a side. As the bicycle starts leaning, the effects we’ve just explored kick in – the front wheel steers into the turn, and the bicycle straightens up or enters a gentle turn.

Stability also heavily depends on the bicycle’s speed – a bicycle that moves too slow _or_ too fast can become unstable. What keeps bicycles balanced with or without a rider is still an active area of research, and even the seemingly basic idea that, for a bicycle to be self-stable, it needs to turn the handlebars into the fall, has not yet been proven.

At this point we’re done describing how forces and moments affect the motion and stability of a bicycle. In the next two sections of this article, we’ll look into the forces transferred _inside_ the components of a bicycle, starting with the parts that give bicycle its name – the two wheels.

# Wheels[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#wheels)

In our discussions so far we’ve only focused on external forces acting on the entire bicycle and the rider. For example, when we looked at gravity, all we cared about was that their weight gets distributed between the **rear** and **front** wheel and then it’s countered by the **reaction** **forces** from the ground:

While this level of detail was useful for analyzing what happens to the bike and rider as a single unit, it unfortunately hides the interactions between the individual components of the bike. It’s time we start looking at these _internal_ forces.

If we pay a close attention to how this bicycle is constructed, we can notice that the weight of the rider and the bicycle frame actually rests on the axles of the wheels, and it’s those axles that push back on the frame and the rider to prevent them from falling down. Let’s separate these components to visualize these inner forces:

Both wheels experience similar loads, just of a different magnitude, so let’s focus on the rear wheel. It’s worth pointing out that while the **red** and **blue** forces have the same magnitude, and the **green** and **white** forces are also equal, but the **red** _and_ **green** forces are _not_ equal, because the wheel **carries** part of the weight of the frame and the rider, but the ground also has to **support** the weight of that wheel. Thankfully, that difference is quite small as wheels are quite light.

With these forces exposed we can now see that a bicycle wheel is _compressed_ between the **force** acting on that wheel’s axle and the **reaction force** from the ground. In three dimensions we can now show that each end of the axle **carries half** of the total load we put on that wheel:

Notice that most of the wheel is completely empty, and it’s only the thin spokes that connect the outer and inner part of the wheel together. The position of the spokes and their attachment points may seem arbitrary, but they’re carefully designed to make the wheel sturdy, reliable, and lightweight.

To understand the design and construction of this modern bicycle wheel we first have to go back in history and look at the wheels used in some of the [early precursors](https://en.wikipedia.org/wiki/Dandy_horse) of bicycles. In the demonstration below, you can assemble a simple wheel one could find in vehicles built in a bygone era:

This wheel consists of the central **hub**, eight rounded **spokes**, and four arched **felloes**. These wooden parts are then wrapped with an **iron rim**. In its normal state, that **rim** is a little undersized and it has to be heated before assembly – after cooling down it shrinks to keep all the pieces tightly together. The **hub** rests and rotates on the **central axle**.

When a wheel like this is **loaded with weight**, the **hub** presses down on the **spokes** in the bottom part of the wheel, and each **spoke** gets **compressed**. As the wheel rotates, different **spokes** become loaded and unloaded:

Notice that in this wheel, the top **spokes** don’t carry any load because they are only loosely inserted into the holes in the **hub** – the spokes can slide out with any pulling force.

These spokes work like little columns that resist the **compressive forces**. Intuitively, the thicker the spoke, the bigger force it can handle before breaking. To compare loads on differently sized objects we use the concept of [_stress_](https://en.wikipedia.org/wiki/Stress_(mechanics)) denoted with lowercase Greek letter sigma **σ**. For pure compressive loads that stress is simply equal to the pushing force **F** divided by the cross section area **A**:

σ =  F / A

Let’s experience this directly. In the demonstration below, you can control the **cross section** of a solid wooden cylinder and the magnitude of a **compressive force** applied to its ends.

You’ve probably noticed that, when compressed, the cylinder gets a little shorter. That shrinkage is proportional to the [properties of the material](https://en.wikipedia.org/wiki/Young%27s_modulus) and the stress **σ** the rod experiences. That’s why a [thicker rod](#) shrinks less than a [thinner rod](#) with the same **compressive force** – its **cross section** is bigger, so the stress is lower, which results in a smaller size change. As a side note, the stress is expressed in units of [pressure](https://ciechanow.ski/naval-architecture/#pressure), so we’ll use _pound per square inch_ or psi_megapascals_ or MPa for short.

With a fixed amount of **force**, the smaller the cross section the bigger the stress. Every material has a certain limit of stress after which it will either [_yield_](https://en.wikipedia.org/wiki/Yield_(engineering)) and deform irreversibly or downright break. However, this also means that all stresses that are kept at a safe margin _below_ these critical limits are permissible to use. As a result, as long as we stay away from the danger zone, we can actually make the spokes thinner and _increase_ the stresses in them for the purpose of saving weight.

Unfortunately, if we make spokes in our wooden wheel too thin we’ll open ourselves up to a nasty surprise. In the demonstration below, you can witness what would happen to a wheel with thin wooden spokes as the hub is **loaded**:

The thin **spokes** _buckle_ under compressive load and the axis drops down a lot – a further increase in the pressing force could cause the **spokes** to break completely.

This buckling behavior is not restricted to wood. Any slender column, even one made from steel, would buckle when compressed with a large enough **force**:

While thin and long objects aren’t effective at resisting forces pushing them on both ends, they’re typically much better at handling forces that want to stretch them. You can easily experience this yourself – a single strand of uncooked spaghetti provides little resistance when gently pressed at its ends, but it’s fairly difficult to break it by just _pulling_ its ends apart.

Thin metal rods are no different. In the demonstration, below you can apply a **pulling force** on a rod and see how it reacts to that **force**, depending on the rod’s **cross section**:

When this thin rod is **pulled** like a string, its tension increases and we say that it is experiencing a _tensile_ load. These forces also create stress **σ** that, just like compression, depends on the magnitude of this force **F** and the cross section **A** of the stretched rod:

σ =  F / A

In the previous demonstration we’ve used relatively small loads, and the rod effectively acted like a very stiff spring that returns to its original shape when unloaded, but when the stresses grow too high, these rods would also eventually yield and break. More importantly, however, that critical tensile load is _significantly_ larger than a compressive load at which this rod buckles.

Let’s try to exploit the pulling resistance of metal rods by building a lighter, modern bicycle wheel. Firstly, instead of thick wooden spokes, we’ll use thin steel spokes. Each spoke has a little **bent knee with a flat cap** at one end, and a **screw-like thread** on the other end:

We also need a new **hub** that will be the central part of the wheel. The **spokes** can be guided through the holes in the new hub, with the little knees acting like little hooks and the caps preventing spokes from going completely through:

The aluminum **rim** forms the outer part of the wheel. It has a set of openings through which the threaded ends of the **spokes** can go. Notice that the spokes are so thin that they can be easily bent by hand to get into a hole:

The threaded end of a **spoke** is capped with a so-called **nipple**, which also has a thread inside. In the demonstration below, I made the **rim** semitransparent, so that you can see how these parts interact. At first, let’s just loosely screw the **nipples** onto the **spokes** right until the point where the **nipples** meet the **rim**:

Let’s see what happens if we now put a **vertical load** on this wheel with **nipples** just loosely tightened:

When we increase the **load**, the **hub** is mostly **pulling** on the spokes in the top part of the wheel. As the **rim** deforms and flattens in its bottom part, the **spokes** and **nipples** in that area just fall through the holes in the **rim**. Those bottom **spokes** are simply dangling from the **hub** without supporting any of the **load**, but even if the **nipples** were somehow locked to the **rim**, these **spokes** would just buckle.

While seemingly functional, a wheel like this wouldn’t be very useful – the axis of the wheel drops a lot, and the deformation of the **rim** is quite severe. With large enough load, the **rim** _itself_ could buckle. We could make the **rim** sturdier and thicker to limit these deformations, but that would also increase its weight.

Notice, however, that the large number of **spokes** doesn’t participate in the load bearing at all. If we could make sure that these spokes are working too, we’d potentially distribute the **pulling forces** more evenly, which would help the **rim** maintain its circular shape.

To understand how we can achieve that, let’s take look at the cross section of the parts to see the interaction between a **spoke**, a **nipple**, and the **rim**, as the **nipple** is screwed with the slider:

As we turn the **nipple**, it initially moves further down onto the **spoke**, but it eventually gets stopped by the **rim**. At that point the **nipple** braces against the **rim** and it starts pulling on the **spoke**, trying to screw it into itself. The **spoke** gets pulled _into_ the **nipple**.

If we just turn a single **nipple**, its **spoke** will simply move the **hub** with it, but if we turn _all_ the **nipples** we can cause all the **spokes** to be under tension and pull with more or less the same **force**:

The **rim** stays rounded because the **tension** of the **spokes** is well balanced across the entire circumference, which keeps the whole structure tightly together. Even without any external forces every spoke is already under tension, because it’s **pulled** between the **hub** and the **rim**. By principle of reaction, it’s also pulling back on these parts – this is all similar to how in a game of tug of war the rope’s ends are pulled away from each other, but the rope also pulls the players _towards_ each other.

For the sake of clarity, let’s visualize these **internal forces**, because sometimes we’ll care about the forces on the **spokes**, and sometimes the forces on the **rim** and the **hub** will be important to us:

Because a **spoke** can freely rotate in its hole in the **hub**, and a **nipple** can freely rotate like a ball in the **rim**, these tensile loads are the only forces that the **spokes** can carry.

Let’s see what happens when we then **load** this wheel. In the demonstration below, you can witness how a **weight** applied on the **hub** ends up distributing over the **spokes** as the wheel rotates. Note that I’m only visualizing the _additional_ **forces** induced by the **weight** _without_ showing you any of the preexisting tension:

A **vertical load** put on a wheel primarily tries to **compress** the few **spokes** under the **hub**. It’s almost impossible to see, but the other **spokes** are also gently pulled on as the **hub** is pushed downwards.

To see the _total_ forces that the spokes experience, we need to add these weight-induced forces to the tension forces already present in the spokes:

Notice, that although the bottom spokes are compressed by the **load**, that compression just reduces the initial tension that we applied by turning the nipples. All the spokes are still **getting pulled**, but as the wheel turns, some of the spokes experience _less_ tension.

It’s mostly the few spokes directly under the **hub** that carry most of the load through a decrease in their tension – all the other spokes just very gently increase their tension. Naturally, without the spokes in the upper part of the wheel the lower ones couldn’t do their work, so ultimately _all_ the spokes serve an important role in keeping a bicycle wheel functional.

You may have noticed that we’ve been rolling the **rim** directly on the ground without the tire present. A pressurized tire will deform much more easily than a **rim**, but ultimately all the forces acting on a tire are carried onto the **rim** too. By removing the tire, we can just focus on the rim and spokes themselves.

In principle, the wheel we’ve built could handle _pure_ vertical loads just fine, but when biking there are also other forces at play. As we’ve seen, when a bicycle is turning, it’s the **side forces** generated by the tires that make the bicycle change its direction:

In a wheel, that force ends up pushing sideways on the tire, which then transfers that load onto the **rim**. Let’s see what happens if we apply a **side force** to the wheel that we’ve assembled so far:

While the **hub** doesn’t move relative to the rest of the bike, the **rim** quite easily deflects from its original plane, which I’m showing with the semi-transparent circle. While some amount of deflection is always expected, if the **rim** tilts too much, it can start rubbing on the other parts of the bicycle, which could prevent the wheel from rotating.

To remedy this we first have to see what happens to the spokes as the **rim** gets deflected. In the demonstration below, you can see a side view of two **neighboring** **spokes** attached to the **rim** and the **hub**. In the bottom part of the demonstration I’m drawing the same **two** **spokes** side be side letting you can compare their lengths as the **rim** gets **deflected** with the first slider:

The second slider controls the **“thickness” of the hub**, which affects the distance between the spokes' attachment points. To allow the **rim** to deflect by a certain amount, the **two** **spokes** have to change their lengths much more when the [hub is wide](#) than when the [hub is narrow](#).

By elongating a spoke we make its pull on the **rim** stronger, and by shrinking it we reduce the pretension, which makes its pull on the **rim** weaker. When we tilt the **rim**, the force imbalance in the spokes makes them want to prevent that deflection by pulling the **rim** back in place. Overall, the bigger the difference in lengths of the spokes, the more strongly they resist the deflection of the **rim**.

For a [narrow hub](#) the spokes' lengths don’t change that much as the **rim** tilts, so even a small side force can easily deflect the **rim** pretty far, before the forces in spokes prevent any further displacement. For a [wide hub](#), the spokes change their lengths much more quickly as the **rim** deflects, so they will be able to resist the force pushing on the **rim** at much smaller **rim** displacement.

We can experience these effects in the demonstration below, where you can adjust the **thickness of the hub** and see how it affects the deflection of the **rim** for a given **side force**. Notice that in practice we’re adding thickness by offsetting a second _flange_ onto which the spokes on the other side of the wheel are attached – we now have **left** and **right** set of spokes:

As you can see, by keeping the spokes at the hub [further apart](#) we make the wheel significantly more resistant to **side loads**. By making the **hub** wide enough we end up with a modern wheel, with spokes arranged in a so-called _radial_ configuration.

One could hope that this was the final step of building a bicycle wheel. If we were to use our creation as a front wheel of a bike with typical caliper brakes, we’d indeed be done. However, to get a fully robust _rear_ wheel we still have one more improvement to make.

To understand the problem we need to solve let’s look at what it takes to make this wheel rotate. In the demonstration below, you can grab one of the **gray points** on the rim of the wheel and then drag it in any direction. Once you let go, I’ll apply a short-lasting force that pulls on the wheel in that direction. The longer the dragging distance, the bigger the force:

Notice that when you apply the **pulling force** directly towards the axis of rotation in the middle of the **hub**, the wheel starts turning very slowly, even when the applied **force** is very big. However, when you pull in the tangent, or perpendicular to the “towards-center” direction, it’s much easier to make this wheel rotate.

The difference in that behavior can be easily explained when we look at the effective radius at which the **pulling force** acts. In the demonstration below, you can observe how the angle of the applied force changes that **radius**:

The smaller that **radius**, the smaller the arm force and thus the resulting torque on the rim, which makes the wheel rotate more slowly. Let’s look at how these concepts translate to the rear wheel of a bike.

When a rider pedals, the chain pulls the sprocket attached to the **hub**, which exerts a torque on that **hub**. The **hub** will rotate a little relative to the **rim**, which changes the location of the inner ends of the **spokes**. This makes the **spokes** a little longer, which increases their tension, but it also creates a tiny **arm** on which the **spokes** can act to turn the **rim**. Let’s visualize that **force** exerted by one of the **spokes** on the **rim**:

Recall, that the **spokes** can rotate in their holes, so they can only apply forces along the length of the spoke itself. Here, however, lies the problem. As we’ve already seen in the wheel turning demonstration, because of that tiny **arm**, these new forces will have a very hard time rotating the **rim**.

If we only cared about rotating the **rim** itself then our existing arrangement of **spokes** would be good enough as the **rim** is quite light. However, when the **hub** is forcibly turned by the pedaling action, the **spokes** attached to that **hub** have to pull and accelerate not only the relatively light **rim**, but that wheel also has to accelerate the entire bike _and_ rider, which is a significantly harder task. That difficulty manifests in an increased spoke tension and [rim stresses](https://www.comsol.com/blogs/why-do-road-and-mountain-bikes-have-different-spoke-patterns/), so radial spokes are very rarely used on a rear wheel.

To make it easier for the **hub** and the **spokes** to rotate the **rim**, we have to make sure that the effective arm length at which the **spokes** pull the **rim** is larger. We can easily do that by using longer **spokes** that are positioned away from the radial direction by applying some twist to the **hub**. Firstly, let’s just set things up using bare long spokes:

Unfortunately, if we then screw on the **nipples** and try to build up tension in the **spokes**, that pulling force would just rotate the **hub** back, preventing any tension from building up until the spokes are back at the radial configuration:

The brilliant solution that bicycle wheel designers came up with is to _flip_ the orientation of every other spoke. Let’s remove the **nipples** and rearrange half of the spokes to point in the other direction:

If we now put the **nipples** back in and we tighten them, one half of the spokes wants to rotate the **hub** clockwise, and the other half wants to rotate the **hub** counterclockwise, keeping everything in balance and allowing the **tension** in the spokes to build up:

This configuration uses a so-called “3 cross” because each spoke crosses three other spokes on its way from the **hub** to the **rim**. This and other patterns form a family of _tangential_ lacing, because the spokes are, more or less, tangent to the **hub** circle instead of coming out of it radially.

With all the pieces in place, let’s see how external loads end up affecting the **tension** in the spokes. With just the **weight load**, these spokes behave very similarly to radial spokes, with the spokes close to ground contact carrying the vast majority of the **load**:

With every turn, each spoke passing under the axle gets loaded and unloaded. This contributes to [mechanical fatigue](https://en.wikipedia.org/wiki/Fatigue_(material)) of spokes, which over a long period of time can eventually cause the spokes to snap.

When the rider is pedaling and a torque gets applied on the **hub**, the **“trailing” spokes**, which are pulled by the **hub** increase their tension, and the **leading spokes** decrease their tension:

Our bicycle is using the traditional caliper brakes that squeeze the **rim**, which results in friction that applies torque to that **rim**. Some bicycles use [disc brakes](https://en.wikipedia.org/wiki/Bicycle_brake#Disc_brakes), which work by applying torque directly on the **hub**. These braking systems apply forces similar to pedaling, just in the other direction, which also prevents use of radial spokes in those bicycles.

Finally, let’s explore how a **side force** that a wheel experiences during turns affects the **tension** in the spokes:

During a ride the spokes experience a mix of all of these loads, many of them happening at the same time. Spokes are typically pretensioned strongly enough so that none of them lose tension when riding, but during an accident the damaging loads can exceed the safe limits and the wheel can collapse and bend under radially unbalanced tension. Interestingly enough, tightening the spokes too much is also unsafe, as they can snap under too much load or cause the **rim** to buckle.

Some high-end bicycle wheels abandon the traditional tensioned spokes and instead use a [shell-like structure](https://en.wikipedia.org/wiki/Bicycle_wheel#/media/File:Carbon_composite_MTB_wheel.JPG) – these rims work similar to the traditional wagon wheels, but the carbon composites used for their construction allows them to be very lightweight.

As we’ve seen, the spokes in a modern bicycle wheel are always being pulled, so the stresses they experience are of a tensile nature. In the last part of this article we’ll look into bicycle frames to see how they handle a whole range of other kinds of stresses.

# Simple Frame[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#simple-frame)

Let’s take a look at the shape of a typical bicycle frame:

A frame like this is commonly made from steel or aluminum tubes of different lengths and diameters that are welded together to form a single, rigid structure.

Fundamentally, a bicycle frame has to provide support and mounting place for four major points of interest: **the seat**, **the rear axle**, **the crankset**, and **the rotation axis** of the fork:

It may be then a little puzzling why a typical frame connects these four locations with two triangular patterns. After all, there are many other ways one could join these points to form a frame:

Moreover, it may be unclear why the tubes forming the frame are hollow, and why their diameter varies across different sections of the frame.

Let’s try to understand what factors influence the design of a bicycle frame by trying to build one from scratch. We’ll keep the wheels, pedals, seat, and the entire front assembly as is – the shape and placement of these components have been perfected over the years to ensure that the bike is stable and that they fit the human anatomy well.

We’ll start with a very simple idea of a cross-like frame shape constructed from solid steel rods. The slider controls the **diameter** of these rods – you can see their cross section in the bottom right corner:

In the bottom part of the demonstration you can see the total weight of the frame as constructed. The thinner the rods in the frame, the lighter the bike and the easier it is to accelerate and slow down, so we definitely want to keep the rods as thin as possible.

This simple frame joins all the important parts we care about, so it would appear that it could work just fine, but this scenario doesn’t consider any loads one can put on a bike. Let’s see what happens to this frame when we load it up with the **weight of the rider** on the seat:

Even though the frame is made from steel, it’s not perfectly rigid and it bends when **loaded**. Although _some_ amount of deflection is unavoidable in any frame, there are also hard limits that we can’t cross. For example, if the frame sinks too much, it may prevent the pedals from rotating without hitting the ground.

Unfortunately, the amount of deflection under typical load is not the only concern we have when designing a bicycle frame, but to understand these other considerations we need talk about bending.

# Bending[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#bending)

Let’s start with a simple example. In the following demonstration you can use the slider to apply a **moment of force** at the two ends of a **beam** made of metal – you can choose _which_ metal using the control below:

The **applied moment** bends the **beam** – it becomes curved. While the material from which the **beam** is made affects _how much_ it bends, the nature of the bending behavior is identical, so we’ll just focus on simple steel elements.

Let’s take a closer look at what happens to different sections of a beam when they’re bent. In the demonstration below, you can once more apply a **bending moment** to the beam to see it deform, but I’m also drawing colored lines on its side. The bottom part shows the same lines that have been straightened out, but kept at the same length as the lines in the top part. Notice that when we bend this beam its **top sections** become shorter and its **bottom sections** become longer.

The upper parts are shortened so they’re under **compression** – bending squeezes these areas. The lower sections of the beam are getting longer so they’re under **tension** – bending stretches these sections of the beam.

Notice, that there is also a dashed _neutral_ line that doesn’t change its length as we bend the beam. For this simple rectangular cross section the neutral axis goes right through the middle of the beam, but in more complicated forms the different distribution of pushing and pulling sections may shift this neutral line away from the midpoint.

In our discussion of wooden and steel spokes we’ve witnessed how **compression** and **tension** create stresses in a material and these beams are no different. In the demonstration below, you can bend the same beam using an adjustable **bending moment**. Different sections of this beam are colored accordingly to the stresses they experience – either **increasing tension**, or **increasing compression**:

As we’ve seen, the further away from the neutral axis a slice of the beam is, the more it changes its length, so the forces it exerts are larger, and so are the stresses. If these stresses grow too big, the beam can deform permanently, or even break completely.

At first glance, it may appear that we should change the cross section of our beam to move the material closer to the neutral axis to make sure it’s not overstressed. In fact, we want to do the exact _opposite_.

In the demonstration below, you can see a closeup of a small part of a beam and the forces exerted by a slice of it – you can control the location of the **investigated slice** with the slider. Notice that the **forces** that a slice exerts act at a **small arm**, thus creating a counter-moment that opposes the **bending moment**:

The sum of the moments exerted by **every slice** of the beam is what balances the **external bending moment**. If we were to move one of these slices further away from the neutral axis, we would not only increase the arm length at which this slice exerts its force, but that force would also grow larger since the slice would get stretched more, as it would have to fit a longer arc.

Both the arc length and the force arm are proportional to the distance from the neutral line, so the moment that a slice exerts grows with a _square_ of that distance. A beam slice placed further away from the neutral axis is more effective at countering the **bending moment**, so by moving it away, the overall curvature and the elongation of individual slices would decrease too.

Let’s see this behavior in practice. In the demonstration below, you can change the **proportions** of the beam to make its cross section shorter or taller. Throughout these changes I’m keeping the area of that cross section the same, which means that the beam’s mass doesn’t change, we’re just redistributing that mass around:

Notice that a [wide and flat](#) slab bends very easily and experiences **high** **stresses**, but a [narrow and tall](#) one barely changes shape and is also **lightly** **stressed**. You’ve probably experienced this yourself trying to bend a school ruler – it’s much easier to do it in one direction than the other.

While these tall shapes are great at resisting bending in one direction, they’re naturally weak in the perpendicular direction. A turning bicycle undergoes side loads too, so the elements we use for building a frame have to be capable of handling forces in multiple directions, which requires a more proportional shape. We also don’t want our bicycle frame to have sharp edges, which brings us back to the solid round rods we’ve initially used for our frame. Let’s see the stresses and deformation in rods of different **diameters** as we apply a **bending moment**:

These rods are no different than the square beams we’ve seen before – the sections furthest away from the neutral axis carry the most load. Conversely, the sections closest to center carry the _least_ load. In fact, we can completely remove these central sections of the rod and move that material more to the outside – instead of solid rods, we’ll use hollow tubes.

In the demonstration below you can control the **hollowness** of a simple rounded rod. I’m keeping the area of the rod’s cross section constant so that as the radius of the tube grows, the walls get thinner. This also means that all the tubes used in this demonstration have the same mass:

By increasing the tube’s diameter and thinning its walls, we’re making it more resistant to bending. It may seem that by making the walls very thin and the tube diameter very large we could make this cylinder arbitrarily strong, but if the walls are _too_ thin they’ll simply buckle on the compressed side – you can easily test this by trying to bend an empty aluminum can.

We’ve already seen that the way a beam bends depends on the [geometrical properties](https://en.wikipedia.org/wiki/Second_moment_of_area) of its cross section, the [mechanical properties](https://en.wikipedia.org/wiki/Young%27s_modulus) of the material used, and on the applied loads. That last aspect deserves a little more attention.

In our examples we’ve been bending the rods with a simple moment of force, but the loads on a bicycle frame are a little more complicated, with various forces applied at many different locations. These forces and the moments they create are carried through all the particles in the frame, and each section of the frame ends up experiencing a slightly different load.

Let’s experiment with a simple rod that is loaded with **three balanced forces**. You can change their magnitude using the slider:

Notice that the **tensile** and **compressive** stresses are no longer uniform across the rod’s length. To understand why this happens, we need to draw a diagram of forces acting on that beam, which you can see in the next demonstration. The bottom part shows the same rod, but this time we’re virtually slicing it at the location determined by the second slider, letting us see the forces that the cut part feels:

Notice that neither the whole rod nor any of its parts are moving, which implies that the forces and moments on every section have to be perfectly balanced. This lets us calculate the **internal force** and the **internal moment** that the particles at the sliced location have to exert to keep the remaining section of the beam static.

As you can see, the **bending moment** varies across the length. Since the bending-related stresses are proportional to that **moment**, different sections of the beam experience different amounts of stress.

In general, the forces that a tube in a frame experiences will be quite varied, and every load may cause that tube to be bent and stretched or compressed at the same time. These stresses will combine to form a more complicated distribution. From this point on I’ll stop separating compressive and tensile stresses, and instead I’ll combine them into a single [equivalent stress](https://en.wikipedia.org/wiki/Von_Mises_yield_criterion):

The **brighter** the element the higher the stress. Once more, when these stresses get too high, they can permanently deform or break the material. Let’s see how the concepts we’ve explored here apply to our simple bicycle frame.

# Stresses in the Frame[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#stresses-in-the-frame)

In the demonstration below, you can revisit the previous frame constructed from solid rods with **controllable diameter**. This time, however, I’m also visualizing the stresses in the rods:

I need to note that this analysis is simplified, as we’re only analyzing the stresses within the tubular sections of the frame – we’re ignoring more complicated stress distributions in the joints between these elements. However, it’s still useful for doing the first pass analysis of a frame.

Notice that for a [fully loaded seat](#) we need to increase the **diameter of the rods** quite a lot before we [get rid of the bright spots](#) – they indicate areas of higher stress. Unfortunately, this makes the frame quite heavy.

To reduce this weight we can make the tubes hollow – we’ve seen how this mass redistribution can actually reduce the stresses. In the demonstration below, we’re once again starting with solid rods, but this time we can increase their **diameter**, while also making the walls thinner. I’m keeping the area of the cross section of the pipes constant, which fixes the weight of the frame:

If we make the tube cross sections [large enough](#) we can make this frame handle vertical **seat loads** with little deflection and within the limits of acceptable stress.

However, as we get ready to ride this bike, new problems emerge. In the demonstration below, you can witness what happens to the frame when the rider starts to vigorously pedal by shifting all his weight from the seat to standing on the right pedal:

The pedals are positioned at a certain distance from the frame, so when a pedal is pressed, that distance acts as a lever that tries to twist the frame out of its position, making many of the tubes become more stressed again.

This time, however, the stresses are a little different as the tubes also undergo a _torsional_ deformation. Let’s explore this concept a little closer. In the demonstration below, we’re once again encountering a solid steel rod. Instead of _bending_ it with a force or a moment, we’re applying a **twisting moment** to it:

With a solid rod like this, it’s a little hard to see what’s going on inside of it, so let’s focus on a short section of that rod and employ a magic see-through vision to let us observe how the ring sections of this rod behave. The second slider lets you choose which ring of this rod we’re looking at:

As we **twist** this beam, its different sections become deformed, which you can see by observing the horizontal lines I drew on each ring. Notice that lines in the center are [barely angled](#), but the ones close to the surface are [fairly skewed](#).

The further away from the central axis a part of the rod is, the more deformed it becomes, as it has to sweep a longer arc as it gets twisted. The bigger the deformation, the larger the stress that section experiences:

This stress is a little different than the ones we’ve explored before, as these elements gets [_sheared_](https://en.wikipedia.org/wiki/Shear_stress). These shearing stresses add another contribution to the total stress that frame elements experience.

Notice that the central parts of this solid rod barely get deformed and stressed. This is yet another reason why hollow pipes are practical for reducing mass of a bicycle frame without compromising its load carrying capabilities. You can experience these loads for pipes with the same mass, but **different hollowness** in the demonstration below:

Let’s go back to our bicycle frame. As we’ve seen, despite our clever attempts to use hollow tubes, the frame we’ve built still was experiencing high stresses. If we kept trying to redistribute the mass inside individual tubes, we could eventually end up with a cross-like frame that’s quite robust, but unfortunately heavy.

However, instead of shifting the mass inside the rods, we can shift the mass inside the _frame_ itself. Let’s start by adding three new tubes at the bottom of the frame. To reduce weight we’ll use hollow tubes across the board, so now we can just control their **diameter**:

Conceptually, these new tubes redistribute the mass further away from the neutral bending axis. For [vertical loads](#), the central part of this frame now acts similarly to a very tall element as the upper and lower tubes are quite far apart. For [pedaling loads](#), this new distribution also helps by bracing the sprocket area and preventing bending stresses from accumulating in the central part.

This new design lets us use thinner and lighter tubes, but there are still a few things we can improve. Notice that the tube that supports the seat still can get pretty stressed because the bending moment inside it can grow quite large. Let’s see if we can improve it by changing the location of the central joints using the third slider:

Notice that in the [“classic” configuration](#) we’ve almost completely minimized the stresses from the [weight on the seat](#). While the area close to the sprocket is still somewhat stressed [when pedaling](#), many of the tubes are now _too_ strong for their purpose. Let’s tweak the size of the individual tubes by thinning the ones that are underutilized, and thickening the more stressed ones:

We’ve more or less arrived at the modern bicycle frame. One could take things even further by making the tubes oval to make them more rigid for bending with vertical forces, or by _butting_ the tubes by making them thinner in the central part, while maintaining thicker walls close to joints, where the stresses are larger.

I need to emphasize that we’ve only conducted a very simplified investigation of a bicycle frame. A more rigorous mechanical analysis requires calculation of all the stresses caused by the bending, torsional, and normal loads to make sure that the materials used will not fail with these and other acting forces a bicycle is required to handle. We also haven’t looked at loads in welds connecting the frame elements – these are often one of the more stressed parts of the frame.

While the classic two-triangle “diamond” frame is mostly commonly used, many bicycles tweak that timeless construction by changing position or even removing some of the tubes. All of these changes have to consider the stresses in the final design to ensure that the bike is safe.

Thankfully, the use of computer aided design tools and modern composite materials lets bicycle manufacturers create much fancier frames with different shapes and thicknesses of individual tubes with varied location of their connection points.

# Further Reading and Watching[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#further-reading-and-watching)

Bicycle stability is an actively researched topic, with new [discoveries](http://bicycle.tudelft.nl/stablebicycle/StableBicyclev34Revised.pdf) being made in the last two decades. [Andy Ruina’s lecture](https://www.youtube.com/watch?v=XmDTTVvmm5M) serves as a gentle introduction into the topic before diving into the [canonical paper](http://ruina.tam.cornell.edu/research/topics/bicycle_mechanics/*FinalBicyclePaperv45wAppendix.pdf) on the subject written by a [group of bicycle researchers](http://bicycle.tudelft.nl/schwab/Bicycle/). These collaborators also took a [closer look into some mistakes](http://bicycle.tudelft.nl/stablebicycle/StableHistoryv32Arend.pdf) made by previous inquirers in this area. For a very long but enjoyable and down-to-earth read, I highly recommend Jason Moore’s [PhD thesis](https://moorepants.github.io/dissertation/index.html) on human control of bicycles.

[Matthew Ford](https://dashdotrobot.com) did extensive research of bicycle wheels, which culminated in his [great PhD thesis](https://arch.library.northwestern.edu/downloads/fb4948624) that thoroughly covers theoretical background and experimental results of what happens to spoked wheels under load. Additionally, Matthew wrote a few more [entry level articles on his blog](https://bicyclewheel.info/articles/) and also made a [wheel simulator](https://bicyclewheel.info/wheel-simulator/) that lets you see forces in spokes under different types of loads.

While _exhaustive_ resources on the influence of forces on the motion of bicycles are relatively scarce, in the sibling field of _motorcycle_ physics, Vittore Cossalter’s [Motorcycle Dynamics](https://www.amazon.com/Motorcycle-Dynamics-Second-Vittore-Cossalter/dp/1430308613) serves as a good stand-in. While some of the topics in the book aren’t directly applicable to bicycles, the publication still covers a lot of phenomena relevant to all single-track vehicles.

Finally, [Bicycling Science](https://mitpress.mit.edu/9780262538404/bicycling-science/) by David Gordon Wilson covers many of other bicycle-related topics like human power generation, rolling resistances, and a deeper dive into aerodynamics, all written in a very approachable style.

# Final Words[![](https://ciechanow.ski/images/anchor.png)](https://ciechanow.ski/bicycle/#final-words)

In the real world, the forces that we have conveniently been visualizing with arrows are not directly visible, but their _effects_ are very tangible. Sometimes that action is, quite literally, straightforward, like when we pedal to propel the bicycle forwards. On the other hand, the interplay of forces that keeps a bicycle stable is much more complicated.

All of these forces are ultimately exerted and carried out by individual atoms that move around to affect their neighbors. The interactions of a single particle in the ground, a tire, or a frame, are completely insignificant, but once we accumulate the effects of all the molecules in these bodies, they end up forming a visible manifestation that makes bicycles rideable.

Perhaps the next time you’re on a bicycle, you’ll be able to conceptualize some of those invisible forces that make the ride so enjoyable.
