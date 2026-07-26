---
title: UISplitViewController
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/uisplitviewcontroller/'
original_language: en
published: 2014-11-03
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:4d6a8715a055915c'
translated: false
---

> 原文：[UISplitViewController](https://nshipster.com/uisplitviewcontroller/)　·　NSHipster (Mattt)

# [UISplit​View​Controller](https://nshipster.com/uisplitviewcontroller/)

Written by  [Natasha Murashev](https://nshipster.com/authors/natasha-murashev/)  September 26^th, 2018 ([revised](https://github.com/nshipster/articles/commits/master/2014-11-03-uisplitviewcontroller.md))

In the beginning, there was the iPhone. And it was good.

Some years later, the iPad was introduced. And with some adaptations, an iOS app could be made Universal to accommodate both the iPhone and iPad in a single bundle.

For a while, the split between the two was the _split_ itself — namely `UISplitViewController`. Given a classic master-detail view controller paradigm, an iPhone would display each on separate screens, whereas an iPad would display both side-by-side.

But over time, the iPhone grew in size and the distinction between phone and tablet began to blur. Starting with the iPhone 6+, apps running in landscape mode on the phone had enough screen real estate to act like they were on a tablet.

Although user interface idioms have made way for the broader concept of size classes, `UISplitViewController` remains a workhorse API for writing Universal apps. This week, let’s take a closer look at how we can use it to adapt our UI to a variety of screen sizes.

---

Let’s start with an example of `UISplitViewController` working its magic on a large iPhone:

However, the view doesn’t split when the iPhone is in _Zoomed_ Display mode.

This is one instance of how split views automatically determine when to show split views.

## Split View Controller, from Start to Finish

The best way to understand how to use `UISplitViewController` works is to show a complete example. The source code for the example project in this post [can be found here](https://github.com/NSHipster/UISplitViewControllerDemo).

### The Storyboard Layout

Here’s an overview of what a storyboard layout looks like with a split view controller:

![UISplitViewController Storyboard Layout](https://nshipster.com/assets/uisplitviewcontroller-storyboard-layout-26c3a8c410c6896b0ffc4e35a1b342ea716083702daedfa81f9ad8a0a7a4a9d5b6eb6c39e0119bbaf6a7b1481a667ac2ba9368e06202a5846df22f3d467cd0d9.png)

In order to _master_ this concept, let’s dive into more _detail_.

### Master / Detail

The first step to using a `UISplitViewController` is dragging it onto the storyboard. The next step is to specify which view controller is the master and which one is the detail.

![UISplitViewController Master-Detail Storyboard](https://nshipster.com/assets/uisplitviewcontroller-master-detail-storyboard-e12e6a2084f6dbcd9d8458e52f606d6bd875fa1ced126770735e3eef56f4ce5cc660afdfa4b0a7972185bce834bfec84f733b7a210f65f9eab335072e258c892.png)

You can do this by selecting the appropriate Relationship Segue:

![UISplitViewController Relationship Segue](https://nshipster.com/assets/uisplitviewcontroller-relationship-segue-db58fa2305918be72134fbce4d09781d723a31503d07c170cc13c296f9f60ed003281cc6586f5a788d532952e261d77e4371a18277bd49684e5369ce4ce03af1.png)

The master view controller is typically the navigation controller that contains the list view (a `UITableView` in most cases); the detail view controller is the navigation controller that contains the view that shows up when the user taps on the list item.

### Show Detail

There’s one last part to making the split view controller work: specifying the “Show Detail” segue.

![UISplitViewController Show Detail Segue](https://nshipster.com/assets/uisplitviewcontroller-show-detail-segue-1de46d65fe0fcbec6c1173445f60c41cb824ebfb392f35a57c2b45a6c2907efb1fc8b935920c01c363a16e2c6f2d33459f8f5ee978cd48dcea96238c524baf98.png)

In the example below, when the user taps on a cell in the `ColorsViewController`, they’re shown a navigation controller with the `ColorViewController` at its root.

### Double Navigation Controllers‽

At this point, you might be wondering: _Why do the master and detail view controllers have to be navigation controllers — especially when there’s already a “Show Detail” segue?_.

Well, let’s see what happens when the detail view controller doesn’t have a navigation controller at its root:

![UISplitViewController No Detail Navigation Controller](https://nshipster.com/assets/uisplitviewcontroller-no-detail-navigation-controller-47874aa34cc099c60ce94cf7bc4af2d2ccd52806c3fb9be1dfe36050b3af775e9096dff9f2bbbf300ea4cfb8002fbf140a91aadbd5cb4ece0e9460e09ce8e849.png)

By all accounts, the app would still work just fine. On a large iPhone, the only difference is the lack of a navigation bar when the phone is in landscape mode:

![UISplitViewController No Navigation Bar](https://nshipster.com/assets/uisplitviewcontroller-no-navigation-bar-e31024a954f6036154758b640893f96aca19492e32be594c0d928755252b41065f5101640fc814bebec4703fb467ce1fd1dba4fe4f05966c0bcd261780024e3b.png))

It’s not a big deal unless want your navigation bar to show a title. But this is a deal-breaker on an iPad:

Notice that when the iPad app first launches, there’s no indication that there’s a split view controller at all! To trigger the master view controller, the user has to magically know to swipe left-to-right.

### Adding a Display Mode Button

To resolve this issue, we’re looking for some way to indicate that there’s more to the app than what’s currently on-screen. Luckily, `UISplitViewController` has a `displayModeButtonItem` navigation item, which can be added to the navigation bar to give us the visual indicator we seek:

```
override func viewDidLoad() {
    super.viewDidLoad()

    …

    navigationItem.leftBarButtonItem =
        splitViewController?.displayModeButtonItem
    navigationItem.leftItemsSupplementBackButton = true
}
```

```
- (void)viewDidLoad {
    [super viewDidLoad];

    …

    self.navigationItem.leftBarButtonItem =
        self.splitViewController.displayModeButtonItem;
    self.navigationItem.leftItemsSupplementBackButton = YES;
}
```

_Build and Run_ on the iPad again, and now you get a nice indication of how access the rest of the app:

The `displayModeButtonItem` property lends some nice usability to apps running on large iPhones in landscape mode, too:

By using `displayModeButtonItem`, you let iOS figure out what’s appropriate for the current screen size and orientation. Instead of sweating the small (and big) stuff yourself, you can sit back and relax. 🍹

## Collapse Detail View Controller

There’s one more optimization we can do for the iPhone. When the user first launches the app, let’s make the master view controller display fully until the user selects a list item. We can do that using [`UISplitViewControllerDelegate`](https://developer.apple.com/documentation/uikit/uisplitviewcontrollerdelegate):

```
class ColorsViewController: UITableViewController {
    var collapseDetailViewController: Bool = true

    …

    // MARK: - UITableViewDelegate

    override func tableView(_ tableView: UITableView,
                            didSelectRowAt indexPath: IndexPath)
    {
        self.collapseDetailViewController = false
    }
}

class SplitViewDelegate: NSObject, UISplitViewControllerDelegate {
    …

    func splitViewController(_ splitViewController: UISplitViewController,
                             collapseSecondary secondaryViewController: UIViewController,
                             onto primaryViewController: UIViewController) -> Bool
    {
        guard let navigationController = primaryViewController as? UINavigationController,
            let controller = navigationController.topViewController as? ColorsViewController
        else {
            return true
        }

        return controller.collapseDetailViewController
    }
}
```

```
// SelectColorTableViewController.h

@interface SelectColorTableViewController :
            UITableViewController <UISplitViewControllerDelegate>
@end

// SelectColorTableViewController.m

@interface SelectColorTableViewController ()
@property (nonatomic) BOOL shouldCollapseDetailViewController;
@end

@implementation SelectColorTableViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    self.shouldCollapseDetailViewController = YES;
    self.splitViewController.delegate = self;
}

#pragma mark - UITableViewDelegate

- (void)tableView:(UITableView *)tableView
didSelectRowAtIndexPath:(NSIndexPath *)indexPath {
    self.shouldCollapseDetailViewController = NO;
}

#pragma mark - UISplitViewControllerDelegate

- (BOOL)splitViewController:(UISplitViewController *)splitViewController
collapseSecondaryViewController:(UIViewController *)secondaryViewController
      ontoPrimaryViewController:(UIViewController *)primaryViewController {
    return self.shouldCollapseDetailViewController;
}

@end
```

Now when the app launches on an iPhone in portrait orientation, `ColorsViewController` is in full view. Once the user selects a color (or the app goes into the background), `ColorsViewController` is collapsed again, and `ColorViewController` is displayed:

---

iOS is always adapting to new capabilities from new hardware. When retina screens were introduced, developers could no longer assume that 1pt = 1px. When larger iPhones were introduced, developers could no longer assume a single screen size.

Today, we’re responsible for accommodating several generations or iPhones and iPads, as well as external displays and various accessibility features. This would be a nightmare if it weren’t for the powerful and thoughtful APIs provided in iOS.

`UISplitViewController` may not be the newest API on the block when it comes to adapting to various interface conditions, but it remains a useful tool for quickly creating robust apps.
