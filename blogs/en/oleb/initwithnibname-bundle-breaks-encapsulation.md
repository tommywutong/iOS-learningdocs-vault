---
title: 'initWithNibName:bundle: Breaks Encapsulation'
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/01/initWithNibName-bundle-breaks-encapsulation/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:b2673cc238c53019'
translated: false
---

> 原文：[initWithNibName:bundle: Breaks Encapsulation](https://oleb.net/blog/2012/01/initWithNibName-bundle-breaks-encapsulation/)　·　Ole Begemann

# initWithNibName:bundle: Breaks Encapsulation

**Update January 27, 2012:** Aaron Hillegass himself [blogged about this same topic](http://weblog.bignerdranch.com/?p=129) already in August 2009. Be sure to also read his post. Thanks to [Cédric Luthi](https://0xced.blogspot.com/) for pointing this out to me.

Here is an interesting approach that I recently learned from reading [Joe Conway’s](http://www.bignerdranch.com/instructors/conway_joe) and [Aaron Hillegass’s](http://www.bignerdranch.com/instructors/hillegass.shtml) excellent introductory book [iOS Programming: The Big Nerd Ranch Guide](https://www.amazon.com/iOS-Programming-Ranch-Guide-Guides/dp/0321773772/).

If you have done any iOS programming, you have probably encountered a pattern like this countless times:

```
- (IBAction)openNextView:(id)sender
{
    MyCustomViewController *nextViewController = [[MyCustomViewController alloc]
        initWithNibName:@"MyCustomViewController" bundle:nil];
    [self presentViewController:nextViewController animated:YES completion:nil];
    // or:
    // [self.navigationController pushViewController:nextViewController animated:YES];
}
```

In response to an event (the user tapping a button), we create and initialize a new view controller instance, using the designated initializer of the `UIViewController` class, `initWithNibName:bundle:`. The we present the view controller on the screen. This pattern is ubiquitous in Apple’s documentation and sample code. But is it good code?

# The Name of the NIB File is an Implementation Detail

Does it make sense for a view controller initializer to have an argument for the name of the view’s NIB file? In other words, should the creator of the view controller decide what NIB file it should load its view from? No. As Joe and Aaron mention in the book^[1](#fn:1), the name of its NIB file is an implementation detail that should only concern the view controller itself. Exposing this detail to an outside caller breaks the [encapsulation principle](https://en.wikipedia.org/wiki/Encapsulation_(object-oriented_programming)) object-oriented programming is based on.

Since we usually subclass `UIViewController` to create our own custom view controllers, fixing this design flaw is easy. We just override the standard `init` method and document it to be our new designated initializer. In that method, we hardcode the values for `nibName` and `bundle` and call the superclass’s designated initializer with them:^[2](#fn:2)

```
@implementation MyCustomViewController

// This is the designated initializer
- (id)init
{
    NSString *nibName = @"MyCustomViewController";
    NSBundle *bundle = nil;
    self = [super initWithNibName:nibName bundle:bundle];
    if (self) {
        ...
    }
    return self;
}
```

We must also override the old designated initializer to reroute it to use the new one:

```
- (id)initWithNibName:(NSString *)nibName bundle:(NSBundle *)bundle
{
	// Disregard parameters - nib name is an implementation detail
	return [self init];
}
```

Now, whenever we need to create a new view controller, we just call `init` rather than `initWithNibName:bundle:`.

# One View Controller, Multiple NIBs

In some cases it can actually make sense to initialize the same view controller with different NIB files. The prime example is different UIs for iPhone and iPad that are contained in separate NIB files but served by the same view controller.^[3](#fn:3) But in this case, too, it should be the view controller itself that decides what NIB file to load. The logic for the decision should be placed into its `init` method:

```
- (id)init
{
    NSString *nibName = nil;
    if (UI_USER_INTERFACE_IDIOM() == UIUserInterfaceIdiomPhone) {
        nibName = @"MyCustomViewControllerPhone";
    } else {
        nibName = @"MyCustomViewControllerPad";
    }
    NSBundle *bundle = nil;
    self = [super initWithNibName:nibName bundle:bundle];
    if (self) {
        ...
    }
    return self;
}
```

And even if the logic which NIB file to load depends on an external value that is only known to the creator of the view controller, it is better design to define a custom `init...` method that takes the external value as a parameter than to expose the name of the NIB file directly. For example:

```
// This is the designated initializer
- (id)initWithContext:(MyViewControllerContext)context
{
    // Decide which NIB file to load depending on the value of context
    ...
}
```

# Conclusion

Even though the flaw in Apple’s design of the `UIViewController` initializers is pretty obvious, it never occurred to me before I read about it in the Big Nerd Ranch book. So thanks again to Joe and Aaron for pointing it out. In the future, I will define my own designated initializer for all my custom view controllers and not expose the view controller’s NIB file to outside callers anymore.

1. On page 174 of the second edition. [↩︎](#fnref:1)
2. **Update January 27, 2012:** Several people pointed out to me that, as long as I give my NIB file the same name as my view controller class (I can even omit the `Controller` part), it is strictly not necessary to specify the `nibName` explicitly here. Just call `[super initWithNibName:nil bundle:nil];`. This is true, but I feel the explicit specification of the NIB file adds a lot of clarity. Also note that implicitly passing `nil` does not fix the inherent design flaw. You still have to override `initWithNibName:bundle:` to make sure that no outside caller can specify a different NIB name. [↩︎](#fnref:2)
3. **Update January 27, 2012:** Many readers noted that this contrived example is not the best and I agree. If you name your NIB files following an Apple-specified pattern (iPhone-specific files end in `~iphone.xib`, iPad-specific ones in `~ipad.xib`), you can just specifiy the base filename in code and the NIB loading system will automatically figure out the correct file (this also works for other resources such as images, by the way). This is the better way to distinguish between different resources for the different platforms. Take the sample code above as a general example on how you would let the view controller decide on the correct NIB file name in different cases. [↩︎](#fnref:3)
