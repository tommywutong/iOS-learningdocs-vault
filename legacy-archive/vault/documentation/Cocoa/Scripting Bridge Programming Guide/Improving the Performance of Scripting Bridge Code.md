---
title: Scripting Bridge Programming Guide
apple_id: TP40006104
resource_type: Guide
platform: macOS
topic: Interapplication Communication
technology: null
published: '2008-03-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptingBridgeConcepts/ImproveScriptingBridgePerf/ImproveScriptingBridgePerf.html
archived_at: '2026-07-15T07:18:54.574407Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Scripting Bridge Programming Guide](Introduction%20to%20Scripting%20Bridge%20Programming%20Guide%20for%20Cocoa.md)


[Next](Document%20Revision%20History.md)[Previous](Using%20Scripting%20Bridge.md)

# Improving the Performance of Scripting Bridge Code

Scripting Bridge code is different from most Objective-C code in that it involves two processes—your process and the scriptable application—and uses Apple events as the way for those processes to communicate. Because of this architecture, performance can be an issue. However, there are several things you can do to optimize performance.

Like AppleScript, Scripting Bridge uses Apple events to send and receive information from other applications. However, because sending Apple events can be expensive, Scripting Bridge avoids sending Apple events until it’s absolutely necessary or until you request it.

As described in [Object Specifiers and Evaluation](About%20Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqmznknlto), scripting objects are actually object specifiers that are references locating an object in the target application. When you ask for an object from an application, what you actually get back is a reference to it in the terms of the scripting definition; evaluation of the reference sends an Apple event to the application, which returns a more precise, “canonical” reference. Scripting Bridge improves performance through conservative evaluation of references. Normally, it won't evaluate a reference until you need some concrete data from it, which is always the value of an object’s property. This is called lazy evaluation.

For example, Scripting Bridge won't send an Apple event when you ask for the first disk of the Finder, but it will send an event when you ask for the name of the first disk of the Finder. Listing 3-1 illustrates this behavior.

__Listing 3-1__  An example of lazy evaluation

```objc
- (IBAction)doTest:(id)sender {
    FinderApplication *finder = [SBApplication applicationWithBundleIdentifier:@"com.apple.finder"];
    SBElementArray *disks = [finder disks];
    FinderDisk *disk = [disks objectAtIndex:0];
    NSString *name = [disk name]; // lazy evaluation occurs
    NSLog(@"Name of first disk is %@", name);
}
```

Most of the time, this lazy evaluation of references won't make much difference to you. However, sometimes you need to be careful to ensure that you get the behavior you expect. Consider the code in Listing 3-2.

__Listing 3-2__  Effect of elapsed time on lazy evaluation

```objc
- (IBAction)doTest:(id)sender {
    iTunesApplication *iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
    iTunesTrack *savedTrack = [iTunes currentTrack];
    sleep(600);
    NSLog(@"Current track is %@", [savedTrack name]);
}
```

At first glance it might appear that this code logs the name of whatever track was playing 10 minutes ago when it gets to the bottom line. Instead the code logs the name of whatever track is _currently_ playing. Why is this so? Recall that Scripting Bridge deals merely with references to objects until you actually need some concrete data from them. So what `savedTrack` stores is a reference to whatever track is currently playing. This reference is evaluated and data is returned only when you call the `name` method, which happens 10 minutes later.

But what if that's not what you want? What if you want the current track “now"? For this, you need to force the current-track reference to be evaluated as soon as it is created.

To force evaluation you use the [get](https://developer.apple.com/documentation/scriptingbridge/sbobject/1423965-get) method, which is declared by `SBObject`. In effect, the `get` method tells Scripting Bridge "stop being lazy—I want you to evaluate this object now." The following code slightly revises the code in Listing 3-2 to use `get` and thus change the resulting track name:

```objc
- (IBAction)doTest:(id)sender {
    iTunesApplication *iTunes = [SBApplication applicationWithBundleIdentifier:@"com.apple.iTunes"];
    iTunesTrack *savedTrack = [[iTunes currentTrack] get];
    sleep(600);
    NSLog(@"Current track is %@", [savedTrack name]);
}
```

Because this code uses the `get` method, `savedTrack` always holds a reference to the track that was playing when the `get` method executed.

Although you may not want Scripting Bridge to be lazy in a particular situation, its lazy evaluation of references dramatically reduces the number of Apple events that need to be sent. Consequently, your application can run significantly faster than it would otherwise. However, if you're not careful about how you write your code, you might needlessly bypass Scripting Bridge's laziness, thus forcing it to send more Apple events than necessary. The following are two common errors:

- __Calling the__ `get` __method when you don’t need to__. Scripting Bridge is excellent at determining when it needs to send an Apple event to get the concrete data you want. When you write `[someObject name]`, for example, Scripting Bridge automatically sends an Apple event to fetch the object's name. If you instead write `[[someObject get] name]`, you force Scripting Bridge to send two Apple events instead of one.
- __Sending the same message multiple times__. Every time you ask an object for the value of a property—such as its name—you force an Apple event to be sent. Thus, in the following example, up to three Apple events might be sent:

```objc
- (IBAction)doTest: {
    FinderApplication *finder = [SBApplication applicationWithBundleIdentifier:@"com.apple.finder"];
    SBElementArray *disks = [finder disks];
    if ([[[disks objectAtIndex:0] name] isEqualToString:@"Macintosh HD"]) { // 1st AE sent
        NSLog(@"The first disk's name is Macintosh HD");
    } else if ([[[disks objectAtIndex:0] name] isEqualToString:@"Disk 1"]) {
        // If execution reaches here, second Apple event sent
        NSLog(@"The first disk's name is Disk 1");
    } else if ([[[disks objectAtIndex:0] name] isEqualToString:@"My Disk"]) {
        // If execution reaches here, third Apple event sent
        NSLog(@"The first disk's name is My Disk");
    }
}
```

  To guarantee that only a single Apple event is sent, call the `name` method only once and store the value in a variable.

```objc
- (IBAction)doTest: {
    FinderApplication *finder = [SBApplication applicationWithBundleIdentifier:@"com.apple.finder"];
    SBElementArray *disks = [finder disks];
    NSString *name = [disks objectAtIndex:0];
    if ([name isEqualToString:@"Macintosh HD"]) {
        NSLog(@"The first disk's name is Macintosh HD");
    } else if ([name isEqualToString:@"Disk 1"]) {
        NSLog(@"The first disk's name is Disk 1");
    } else if ([name isEqualToString:@"My Disk"]) {
        NSLog(@"The first disk's name is My Disk");
    }
}
```


Scripting Bridge optimizes `SBElementArray` objects as well as `SBObject` objects by making them lazy when it comes to Apple events. They don’t send any Apple events until absolutely necessary. When you manually iterate through an `SBElementArray` object, however, you force Scripting Bridge to send as many Apple events as there are items in your array. Take the following example, which makes a list of the name of every disk in the Finder:

```objc
- (IBAction)doTest:(id)sender {
    FinderApplication *finder = [SBApplication applicationWithBundleIdentifier:@"com.apple.finder"];
    SBElementArray *disks = [finder disks];
    NSMutableArray *nameArray = [NSMutableArray arrayWithCapacity:[disks count]];
    for (FinderDisk *currentDisk in disks) {
        [nameArray addObject:[currentDisk name]];
    }
```

This code is extremely inefficient. It requires Scripting Bridge to send an Apple event to obtain the number of disks. Then, each time through the fast-enumeration loop, it sends an additional Apple event to get the name of the current disk.

As discussed in [Using Element Arrays](Using%20Scripting%20Bridge.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dcmbufvbuqnbnknltcmq), whenever possible you should always use one of the “batch operation” array methods instead of enumerating the array. These methods avoid the inefficiency of enumeration because they send a single Apple event rather than one Apple event per item in the array. The methods to use are [makeObjectsPerformSelector:withObject:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/makeObjectsPerformSelector:withObject:) and [filteredArrayUsingPredicate:](https://developer.apple.com/documentation/foundation/nsarray/1411033-filtered) of `NSArray`, and [arrayByApplyingSelector:](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1423951-arraybyapplyingselector) and [arrayByApplyingSelector:withObject:](https://developer.apple.com/documentation/scriptingbridge/sbelementarray/1424007-array) of `SBElementArray`.

For example, you could rewrite the method above as shown in Listing 3-3.

__Listing 3-3__  Processing an array with `arrayByApplyingSelector:`

```objc
- (IBAction)doTest:(id)sender {
    FinderApplication *finder = [SBApplication applicationWithBundleIdentifier:@"com.apple.finder"];
    SBElementArray *disks = [finder disks];
    NSArray *nameArray = [disks arrayByApplyingSelector:@selector(name)];
    // or you could use valueForKey: (NSArray), e.g.
    // NSArray *nameArray = [disks valueForKey:@"name"];
}
```

This code sends only a single Apple event.

If an application isn’t executing when Scripting Bridge tries to send it an Apple event, Scripting Bridge may automatically launch it. The launch of the other application may come as a surprise to your users, along with the fact that you application’s execution is blocked while the other application is launching.

Because of these potential surprises, it’s often a good idea to check whether the target application is running before you try to communicate with a Scripting Bridge message. Suppose you want to get the name of the current track, but only if iTunes is running. You could accomplish by first testing for application execution with the [isRunning](https://developer.apple.com/documentation/scriptingbridge/sbapplication/1423981-isrunning) of `SBApplication`, as shown in Listing 3-4.

__Listing 3-4__  Testing for application execution

```objc
- (NSString *) nameOfCurrentTrack
{
    // "iTunes" is an instance variable
    if ([iTunes isRunning]) {
        return [[iTunes currentTrack] name];
    }
    return nil;
}
```

[Next](Document%20Revision%20History.md)[Previous](Using%20Scripting%20Bridge.md)

