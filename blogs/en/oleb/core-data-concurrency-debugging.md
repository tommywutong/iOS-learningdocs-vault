---
title: Core Data Concurrency Debugging
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2014/06/core-data-concurrency-debugging/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:27ae975a05a98c8d'
translated: false
---

> 原文：[Core Data Concurrency Debugging](https://oleb.net/blog/2014/06/core-data-concurrency-debugging/)　·　Ole Begemann

# Core Data Concurrency Debugging

In iOS 8 and OS X Yosemite, Core Data gains the ability to detect and report violations of its [concurrency model](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW39).^[1](#fn:1) I think this is a very valuable feature because accessing a managed object context from the wrong queue is a simple mistake to make and can be fatal if it causes your users’ data to get corrupted.^[2](#fn:2)

On the Mac, Core Data [has had the option](https://developer.apple.com/library/mac/technotes/tn2124/_index.html#//apple_ref/doc/uid/DTS10003391-CH1-SECCOREDATA) to debug concurrency issues for a while. However, enabling the feature required developers to manually install a special debug version of the framework, which was frequently not even available because Apple did not keep it up to date. This was not at all a practical solution. For iOS, Apple never released a debug library in the first place.

# Enabling Multi-Threading Assertions

With iOS 8 and Yosemite, the Core Data framework supports concurrency debugging out of the box. It works by throwing an exception whenever your app accesses a managed object context or managed object from the wrong dispatch queue. You enable the assertions by passing `-com.apple.CoreData.ConcurrencyDebug 1` to your app on the command line via Xcode’s Scheme Editor.^[3](#fn:3)

[![Configuring command line arguments in Xcode’s Scheme Editor](https://oleb.net/media/xcode-scheme-core-data-concurrency-debug.png)](https://oleb.net/media/xcode-scheme-core-data-concurrency-debug.png)

<sub>Add the`-com.apple.CoreData.ConcurrencyDebug 1`launch argument to the Run action of your build scheme in Xcode.</sub>

When you launch your app, you should see a message in the console that tells you that the assertions are now enabled:

```
CoreData: annotation: Core Data multi-threading assertions enabled.
```

# How Does It Work?

Let’s set up a very simple Core Data stack to test how this works in practice (in Swift, no less!). I use an in-memory store in this example but it works exactly the same with SQLite. Also note that the fact that I skipped error handling does not mean you should do so, too.

```
let objectModelURL = NSBundle.mainBundle().URLForResource("MyDataModel", withExtension: "momd")
let objectModel: NSManagedObjectModel? = NSManagedObjectModel(contentsOfURL: objectModelURL)
assert(objectModel)

let storeCoordinator: NSPersistentStoreCoordinator? = NSPersistentStoreCoordinator(managedObjectModel: objectModel)
assert(storeCoordinator)

let store: NSPersistentStore? = storeCoordinator!.addPersistentStoreWithType(NSInMemoryStoreType, configuration: nil, URL: nil, options: nil, error: nil)
assert(store)

// Set up a managed object context with private queue concurrency
// backgroundContext is a NSManagedObjectContext? property
backgroundContext = NSManagedObjectContext(concurrencyType: .PrivateQueueConcurrencyType)
assert(backgroundContext)
backgroundContext!.persistentStoreCoordinator = storeCoordinator!
```

The most important thing to note is that I have set up the managed object context as a background context with `.PrivateQueueConcurrencyType`. This means that I am not allowed to access this context from the main queue (or any other queue, for that matter). What happens if I do so anyway? (Again, do not leave out error handling of the `save()` method in your code.)

```
// Work on the background context without using performBlock:
// This should fail because we are violating Core Data's concurrency contract.
let person = NSEntityDescription.insertNewObjectForEntityForName("Person", inManagedObjectContext: backgroundContext!) as NSManagedObject
person.setValue("John Appleseed", forKey: "name")
backgroundContext!.save(nil)
```

When I run this code, execution does not even reach the `save()` call. The framework throws an exception on the first line because I violated Core Data’s concurrency model by calling `.insertNewObjectForEntityForName()` with the private queue context as an argument from the main thread.

[![Xcode 6 displaying a Core Data multithreading violation exception](https://oleb.net/media/xcode-core-data-multithreading-violation.png)](https://oleb.net/media/xcode-core-data-multithreading-violation.png)

<sub>When you violate Core Data’s threading contract, the debugger halts at `+[NSManagedObjectContext __Multithreading_Violation_AllThatIsLeftToUsIsHonor__]:`.</sub>

## A Bug in iOS 8 Beta 1

What I should have done is wrap all access to `backgroundContext` in a block passed to [`performBlock:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW45) or [`performBlockAndWait:`](https://developer.apple.com/library/ios/documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html#//apple_ref/doc/uid/TP30001182-SW46), which executes the block on the context’s private dispatch queue:

```
// Work on the background context with using performBlockAndWait:. This should work.
backgroundContext!.performBlockAndWait {
    let person = NSEntityDescription.insertNewObjectForEntityForName("Person", inManagedObjectContext: self.backgroundContext!) as NSManagedObject
    person.setValue("John Appleseed", forKey: "name")
    self.backgroundContext!.save(nil)
}
```

In my testing with iOS 8 beta 1, this code passes the first assertion but then fails with a multithreading violation on the last line at `self.backgroundContext!.save(nil)`. I believe this is a bug in the current beta of the SDK since I am not violating the threading model. Other people are seeing [the same behavior](https://devforums.apple.com/message/983107). I have reported this to Apple as rdar://17266389 and I hope to get a reply soon.

**Update July 23, 2014:** This bug has been fixed with Xcode 6 beta 4.

# GDCoreDataConcurrencyDebugging

I should also mention Graham Dennis’s [GDCoreDataConcurrencyDebugging library](http://www.grahamdennis.me/blog/2013/09/09/debugging-concurrency-with-core-data/), which uses some clever method swizzling and dynamic subclassing to detect when a managed object is accessed in an invalid way. As far as I can tell, the library watches only messages sent to `NSManagedObject` and not to `NSManagedObjectContext`, but it seems like a great option, at least until Apple fixes the bug I mentioned above.

1. Source: [WWDC 2014 session](https://developer.apple.com/videos/wwdc/2014/) 225, “What’s New in Core Data”. [↩︎](#fnref:1)
2. In fact, [according to Core Data guru Marcus Zarra](https://forums.pragprog.com/forums/252/topics/12271), iOS 6 and OS X 10.8 used to throw an exception for every threading violation, but Apple had to turn that feature off because it would crash too many apps in production. This should tell you how common these mistakes are. [↩︎](#fnref:2)
3. Make sure to check the “Shared” option and add the scheme file to version control if you want to share the scheme with your team. [↩︎](#fnref:3)
