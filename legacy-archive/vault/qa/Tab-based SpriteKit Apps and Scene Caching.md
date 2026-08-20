---
title: Tab-based SpriteKit Apps and Scene Caching
apple_id: DTS40016267
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: SpriteKit
published: '2015-06-23'
source_url: https://developer.apple.com/library/archive/qa/qa1889/_index.html
archived_at: '2026-07-18T02:35:23.254167Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1889

# Tab-based SpriteKit Apps and Scene Caching

## Q:  How can I manage scene memory in a tab-based SpriteKit app?

A: SKView maintains a cache of the scenes it presents for performance reasons but this can cause unexpected memory usage, especially in apps that use multiple SKViews. For example, in tab-based SpriteKit apps, there will eventually be as many scenes loaded in memory as there are number of tabs. This often puts the app in need of managing scene memory manually by deallocating off-screen scenes. Passing a nil argument to SKView `presentScene` does not cause the scene to be freed, instead, to release the scene, you must free the SKView that presented it.

The following are important implementation details relating to the view controller's root view:

1. Replacing a view controller's root view is not recommended, and therefore, apps that set their view controller's root view to an SKView within a storyboard should instead set the root view to UIView, then create the SKView programmatically. The code within this document demonstrates the latter approach.
2. Do not create SKViews in Interface Builder in your storyboard, even if they are embedded in a UIView.

The following listings illustrate the code needed to deallocate off screen SKView's as required to release unused resources allocated by its scene. Using this technique prevents scene caching and allows a tab-based app to run with only the current scene in memory.

1. Implement UIViewController `viewWillAppear` where the SKView will be allocated:


```objc
@implementation TabOneViewController
...
-(void)viewWillAppear:(BOOL)animated {
    if( !self.skView ) {
        NSLog(@"%s - (re)creating skView",__PRETTY_FUNCTION__);
        self.skView = [[SKView alloc] initWithFrame:self.view.bounds];
        [self.view addSubview:self.skView];
        SKScene* scene = [[TabOneGameScene alloc] initWithSize:self.skView.bounds.size];
        [self.skView presentScene:scene];
    }
}
```
2. Implement UIViewController `viewDidDisappear` where the SKView will be deallocated:


```objc
-(void)viewDidDisappear:(BOOL)animated {
    if( self.skView ) {
        NSLog(@"%s - removing skView",__PRETTY_FUNCTION__);
        [self.skView removeFromSuperview];
        self.skView = nil;
    }
}
```

In addition, you may use the following code to confirm that scenes are being deallocated. By adding logging within an overridden implementation of dealloc, you are able to confirm with console logging when a particular scene object is freed. This code logs the address of the object, as a way to uniquely identify the instance.

1. 

```objc
@implementation TabOneGameScene
-(void)dealloc {
    NSLog(@"%s - %p",__PRETTY_FUNCTION__,self);
    // [super dealloc]; // only call super dealloc for non-ARC apps/files
}

...

@implementation TabTwoGameScene
-(void)dealloc {
    NSLog(@"%s - %p",__PRETTY_FUNCTION__,self);
    // [super dealloc]; // only call super dealloc for non-ARC apps/files
}
```
2. Look to the iOS device console within Xcode for the relevant logging while performing the following tests:

   1. Logging after starting the app:


```
TabbedSKViews[457:873673] -[TabOneViewController viewWillAppear:] - (re)creating skView]
```
   2. Logging after switching to tab 2:


```
TabbedSKViews[457:873673] -[TabTwoViewController viewWillAppear:] - (re)creating skView]
TabbedSKViews[457:873673] -[TabOneViewController viewDidDisappear:] - removing skView
TabbedSKViews[457:873673] -[TabOneGameScene dealloc] - 0x5ade50
```
   3. Logging after switching back to tab 1:


```
TabbedSKViews[457:873673] -[TabOneViewController viewWillAppear: - (re)creating skView]
TabbedSKViews[457:873673] -[TabTwoViewController viewDidDisappear:] - removing skView
TabbedSKViews[457:873673] -[TabTwoGameScene dealloc] - 0x753500
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-06-23 | New document that explains SKView's scene cache in order to minimize memory spikes in tab-based SpriteKit apps. |

