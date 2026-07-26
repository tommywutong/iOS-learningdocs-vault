---
title: 'Surprising Weak-Ref Implementations: Swift, Obj-C, C++, Rust, and Vale'
source_url: 'https://verdagon.dev/blog/surprising-weak-refs'
source_domain: verdagon.dev
source_group: single-site
original_language: en
published: ''
archived_at: 2026-07-27
content_hash: 'sha256:1eaae12c3bd3915d'
plan_ref: 第二周：weak、属性关键字与 Block / Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06）
plan_week: 第二周：weak、属性关键字与 Block
plan_day: Day 2｜weak 按“写入—读取—销毁”三段学（对应 W2-01～W2-06）
container: '//div[contains(@class,''page-inner'')]'
container_source: map
---

> 原文：[Surprising Weak-Ref Implementations: Swift, Obj-C, C++, Rust, and Vale](https://verdagon.dev/blog/surprising-weak-refs)

# Surprising Weak-Ref Implementations: Swift, Obj-C, C++, Rust, and Vale

Such shenanigans, right under our noses!

Apr 4, 2022  —  Evan Ovadia

"Are you kidding me? That's... **horrifying.**" - Alice (about Obj-C).

"That's nonsense!" - Ed (about Vale).

"It's not just an index, a weak reference is a **state of mind.**" - Bob (about Rust)

Weak references are _weird_.

This post is a collection of all the mysterious and arcane mechanisms that languages use to offer weak references.

Our quest was to figure out the best approach to use for [Vale](https://vale.dev/), that aligned with its goals of being **fast, memory safe, and easy to use.**

In the end, we made a completely new approach!

## What are they _supposed_ to be?

In most languages, [0](#note0) normal references are "strong". As long as there is at least one strong reference to an object, the object stays alive. When the last strong reference goes away, the object is deallocated. [1](#note1)

We can also have **weak** references to the object, which _don't_ keep the object alive. After the target object dies, they appear to be null. [2](#note2)

These aren't just useful to break [ref-counting cycles](https://www.appypie.com/how-to-fix-strong-reference-cycle-swift). They're also used to know when something still logically exists, to factor into our program's behavior. If you ever seen an alive or dead boolean in a class, you're likely seeing a good use-case for weak references.

For example, we can use it in an observer:

vale

```vale
func handleClick(self &Button) {
  // Check if self.clickObserverWeakRef points to an object that's still alive.
  // If it is, refer to it as clickObserver.
  if clickObserver = self.clickObserverWeakRef.lock() {
    // Now that we know it's alive, call its onClick.
    clickObserver.onClick();
  }
}
```

Or perhaps a magic missile can check if its enemy still exists:

vale

```vale
func takeAction(self &Missile) {
  // Check if self.enemyWeakRef points to an enemy that's still alive.
  // If it is, refer to it as enemy.
  if enemy = self.enemyWeakRef.lock() {
    // Now that we know it's alive, move one step closer to it.
    self.position.goToward(enemy.position);
    if self.position == enemy.position {
      // We've reached the enemy, explode!
      self.explode();
    }
  } else {
    // The enemy is gone. Explode where we are anyway!
    self.explode();
  }
}
```

It's a rather useful tool! And it's pretty simple under the hood.

_...except_ in Objective-C.

## Objective-C's Global Weak Pointer Tracking Manager [3](#note3)

Objective-C has a mutex-guarded global hash map, tracking all the weak references and what objects they point to.

Specifically:

- When we make a new weak reference to an object, we add an entry to the map:
- When we get rid of a weak reference to an object, we remove that entry from the map.
- When an object dies, it looks for all the entries for the object...

Unexpectedly, there _are_ benefits to this approach!

- Given a weak reference, checking if it's pointing at a live object is _extremely fast_. We just have to check if the reference is nil.
- This doesn't have the "zombie allocation" problem that Swift and Rust have; this approach _may_ use less memory than they do.
- Until we make the first weak reference, this approach uses zero overhead.

But of course, it has drawbacks:

- It's _extremely_ slow to create and destroy weak references. It has to obtain a global lock and do some hash map operations.
- Each weak reference costs 16B, sometimes more. [4](#note4)

**Side Notes**

(interesting tangential thoughts)

Notes [–] Notes [+] 0 1 2 3 4

0

More specifically, in shared-ownership languages like Python, Swift, Obj-C, C#.

1

In reference counted languages like Swift, the language immediately notices there are no more strong references to the object, and deallocates the object right away. In tracing-garbage-collected languages like Java, the interpreter eventually notices that nobody points at this object, and deallocates it then.

2

Languages rarely set them to null. More often, a weak reference has some way of knowing whether the target object is still alive, so it can pretend to be null.

3

Sources: [Matt](https://stackoverflow.com/a/42847825), [Mecki](https://stackoverflow.com/a/23689503)

4

I'm not certain, but if the global map is an unordered_map\<void*, vector\<void*\>*\> hash map (in C++ terms) with a load factor of 0.5, then making the first weak reference to a new object could cost ~48B, and any subsequent weak references would cost 16B. If anyone wants to dive in, the source code is available in [this repo](https://github.com/apple-oss-distributions/objc4/tree/objc4-838.1), likely somewhere around [objc-weak.h](https://github.com/apple-oss-distributions/objc4/blob/objc4-838.1/runtime/objc-weak.h). (Thanks to [mayoff](https://www.reddit.com/r/vale/comments/tuokkq/surprising_weakref_implementations_swift_objc_c/i38ln6f/?context=3) for the lead!)

## Swift's Zombie Objects

Update: This description is actually outdated; this article describes how it worked before Swift 4. In Swift 4, they updated it to use "side tables", see [Mike Ash's Post](https://www.mikeash.com/pyblog/friday-qa-2017-09-22-swift-4-weak-references.html) describing them. [5](#note5) Stay tuned for a part 2, where we'll talk about side tables, "reference chaining", and Python's approach!

When Swift isn't using the Objective-C approach for compatibility reasons, Swift actually does something pretty elegant. [6](#note6)

A Swift object has two counters in it:

- A counter which counts how many **strong** references point at the object.
- A counter which counts how many **weak** references point at the object.

Remember how we said "when the last strong reference goes away, the object is deallocated"? **That's not true for Swift.**

Let's say an object has strong references and weak references pointing at it.

When the last strong reference goes away, the object is **deinitialized**, but not deallocated. I like to think that deinitializing just zeroes out all the fields. [7](#note7)

The object isn't deallocated quite yet; the object is in kind of a "zombie state" because it has no usable contents, but it's kept alive while there are still weak references pointing to it.

If we ask one of these weak references "are you pointing at a live object?", it will look into the object and check if the strong ref count is positive. If so, it responds true. If it's zero, it responds false. [8](#note8)

Later, when we let go of the last weak reference, the weak reference counter goes to zero, and the object is deallocated; the zombie is finally destroyed.

Swift's approach has a big benefit:

- It's very fast, because the ref-count is next to the rest of the object's fields, which is very cache-friendly. [9](#note9)

and some costs:

- Zombie objects: the entire object's allocation might stick around even after the last strong reference disappears.
- It has some memory overhead (a second counter per object), which we pay even if we never use weak references.
- All objects must be separately allocated in the heap, we can never have a weak reference to an object that lives inside another object's memory.

Swift's approach is very simple, and I like that. [10](#note10)

Notes [–] Notes [+] 5 6 7 8 9 10

5

Thanks to [electromaster666](https://www.reddit.com/r/swift/comments/tuoduj/surprising_weakref_implementations_swift_objc_c/i37d0u2/?context=3), [mayoff](https://www.reddit.com/r/vale/comments/tuokkq/surprising_weakref_implementations_swift_objc_c/i38ln6f/?context=3), and [jaredgrubb](https://www.reddit.com/r/cpp/comments/tuohau/surprising_weakref_implementations_swift_objc_c/i3b94ws/?context=3) for noticing this!

6

Source: [Mike Ash](https://mikeash.com/pyblog/friday-qa-2015-12-11-swift-weak-references.html)

7

This isn't quite true, it actually doesn't change the memory, but it helps a lot to think of it this way.

8

If the answer is false, Swift also sets the reference to be _actually_ null, rather than just pointing at a zombie object, so it can answer more quickly next time, without having to dereference again.

9

This means that the counters are on the same cache line as the fields, which means if we access the counter, the CPU naturally brings some nearby fields into cache, making subsequent accesses faster.

10

Especially compared to Objective-C's approach!

## C++'s weak_ptr

If we look at the memory layout, C++ is similar to Swift; right next to the object we can have a strong ref count and a weak ref count. [11](#note11)

In C++, we choose whether an object can have weak references to it or not. A Spaceship will by default not have any counters, but a shared_ptr\<Spaceship\> will have them.

We can make a weak reference, a weak_ptr\<Spaceship\>, from any shared_ptr\<Spaceship\>.

This has benefits:

- We can opt-in to the counters' 16B overhead only when we need it. [12](#note12)

And a cost:

- Each weak_ptr is 16B. [13](#note13)

And some oddities:

- If we make the allocation with make_shared, the object and its control struct share an allocation, resulting in zombie objects. [14](#note14)
- If we have a regular pointer (Spaceship*) we cannot get a weak_ptr\<Spaceship\> unless Spaceship inherits from std::enable_shared_from_this.

Notes [–] Notes [+] 11 12 13 14

11

This is the case if we use std::make_shared. If we initialize a shared_ptr directly, then the counters will be somewhere else in the heap.

12

This is a principle called "zero-cost abstraction"; if we don't use a feature, it doesn't cost us any space or CPU time.

13

A typical implementation of weak_ptr stores two pointers:

- a pointer to the control block; and
- the stored pointer of the shared_ptr it was constructed from.

Source: [cppreference](https://en.cppreference.com/w/cpp/memory/weak_ptr)

14

[Source](https://dev.to/fenbf/how-a-weakptr-might-prevent-full-memory-cleanup-of-managed-object-i0i)

## Rust's Weak

Rust's Rc and Weak are basically C++'s shared_ptr and weak_ptr, with a couple differences:

- Rust's Rc always puts its counters next to the object, whereas C++ lets us put it in a separate block if we want to.
- Given a &Spaceship, we aren't able to get a Weak\<Spaceship\>.

We don't often see Rc and Weak in Rust. Instead, we use other mechanisms that behave like weak references.

## Weak References, Hidden in Plain Sight

We've now seen a few different kinds of weak references. However, if we zoom out a bit, we see a lot of things that act very similarly to weak references.

A weak reference is basically something that you can trade for a regular reference to the object _if it still exists_.

When you think of it that way, a lot of things are weak references.

For example, a string containing a filename, like myfile.txt. We can trade it for the contents of a file, if the file still exists:

vale

```vale
func main() {
  if contents = readFileAsString("myfile.txt") {
    // File exists!
    println(contents);
  } else {
    println("File doesn't exist!");
  }
}
```

Or perhaps we have an integer ID, and we can use it to look up a Spaceship in a map:

vale

```vale
func printName(ships &HashMap<int, Spaceship>, ship_id int) {
  if ship = ships.get(ship_id) {
    println("Ship exists! {ship.name}")
  } else {
    println("Ship doesn't exist!");
  }
}
```

Notice how we first check for existence, and then use the resulting data. Just like a weak reference!

My favorite kind of weak-reference-in-disguise is the **generational index**, often used in C++ and Rust programs.

## Generational Indices

We often store our objects in arrays or vectors, such as a Vec\<Spaceship\>. [15](#note15) When we destroy a Spaceship, we often like to reuse its spot for another Spaceship.

Sometimes, we remember a Spaceship's index in the Vec. Later, we might want to know if that Spaceship is still there, or if it's been reused. Here's how!

Next to every object in the vector, we have an integer: Vec\<(Spaceship, i64)\>. That i64 is the Spaceship's **current generation number**. Every time we reuse a slot, we increment that number.

Whenever we want to remember a Spaceship's index, we'll also remember its generation number at the time. This is the **remembered generation number**.

For convenience, let's put the index and this "remembered generation number" in a little struct called a GenerationalIndex:

```
struct GenerationalIndex {
  index: i64,
  remembered_generation: i64
}
struct Missile {
  enemy_ref: GenerationalIndex
}
```

Now, if we want to know whether the Spaceship still exists, we just **compare the current generation number to the remembered generation number,** like:

```
if enemies[missile.enemy_ref.index] == missile.enemy_ref.remembered_generation {
  // Enemy still exists!
  let enemy = &enemies[missile.enemy_ref.index];
  ...
}
```

It's as if the generational index is saying:

**"Hello! I'm looking for the 11th inhabitant of index 7, are they still around?"**

and the element at index 7 says:

**"No, sorry, I'm the 12th inhabitant, the 11th inhabitant is no more."**

or instead:

**"Yes! That is me. Which of my fields would you like to access?"**

That's a generational index. It's like a weak reference!

However, there is one downside to generational indices: to "dereference" it, we need access to the containing Vec (like the enemies Vec above), usually passed in through a parameter.

This can sometimes be inconvenient: when we add a new parameter, we have to change our callers to supply it, and then our callers' callers, and our callers' callers' callers, which can result in "refactoring shockwaves". Doing this too often can cause churning APIs.

Sometimes, to work around this drawback, we give up and put all of our containers into a "god object" and pass that around as an argument to every function in our codebase.

Perhaps there's a better way to address this drawback. Read on!

## Vale's Generational References

Vale adds something like the generational index, which we call a **generational reference**.

Every object has a "current generation number" next to it in memory. Whenever we destroy an object, we increment that number. [16](#note16)

To make a weak reference to that object, we get two things:

- A pointer to the object. [17](#note17)
- The object's current generation number.

...and stick them together.

To know whether the object still exists, Vale just compares the object's current generation number to our reference's remembered generation number.

Similar to the generational index, It's as if the reference is saying:

**"Hello! I'm looking for the 11th inhabitant of this house, are they still around?"**

and the person who opens the door says:

**"No, sorry, I'm the 12th inhabitant of this house, the 11th inhabitant is no more."**

or instead:

**"Yes! That is me. Which of my fields would you like to access?"**

We implemented generational references, and found them to be [at least 2.3x faster than reference counting!](https://verdagon.dev/blog/generational-references)

Compared to the other weak reference approaches, this has benefits:

- Making or destroying new weak references is free, no reference counters need to be incremented.
- It enables [Fearless FFI](https://vale.dev/fearless#safe-externs); C code cannot corrupt Vale objects. [18](#note18)
- It doesn't suffer the zombie object problem.
- Supporting generational references costs an allocation only 8B!

And costs:

- Supporting generational references costs an allocation a whole 8B.
- It can take some virtual memory maneuvers to release memory to the OS. [19](#note19)
- It can only be used for heap allocations, which have stable addresses.

We foresee the average Vale program blending three different approaches:

- For heap allocations, we'd use generational references.
- When we have convenient access to the container, we'd use generational indexes.
- For everything else, we'd use "augmented generational indexes" which also bundle in a reference to the container.

By offering these all in the standard library, we can make it easy to have fast weak references. That's good, because Vale's goal is to make speed and safety easier than ever before.

Notes [–] Notes [+] 15 16 17 18 19

15

Or a C++ std::vector\<Spaceship\> or a Java ArrayList\<Spaceship\>.

16

Note that we don't free() it to the operating system quite yet, because we need that generation number to stick around so we can compare it to weak references' remembered generation numbers. Later on, we release the physical memory back to the OS using some virtual memory techniques. See [Mesh](https://tiba-jrchang.medium.com/mesh-compacting-memory-management-for-c-c-applications-bc2a2cecc8cc) for more!

17

Since it's not an index, we don't need access to any container!

18

Reference-counting approaches such as Python suffer from this. We give a reference to C code, the C code has to manually remember to increment/decrement it. Forgetting to do so will corrupt the Python object. No such incrementing is needed for generational references!

19

See [Mesh](https://tiba-jrchang.medium.com/mesh-compacting-memory-management-for-c-c-applications-bc2a2cecc8cc), an algorithm for merging virtual addresses into one underlying physical page.

## Conclusion

Thanks for reading! In the coming weeks, I'll be writing about how we can augment generational references with an "automatic borrow checker," so subscribe to our [RSS feed](https://verdagon.dev/rss.xml), [twitter](https://twitter.com/vale_pl), or the [r/Vale](https://reddit.com/r/vale) subreddit, or come hang out in the [Vale discord](https://discord.gg/SNB8yGH).

- Evan Ovadia
