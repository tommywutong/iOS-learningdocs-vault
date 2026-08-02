---
title: Finding and Fixing Category Method Name Clashes
apple_id: DTS40016829
resource_type: QA
platform: watchOS|tvOS|iOS|macOS
topic: Languages & Utilities
technology: null
published: '2016-03-23'
source_url: https://developer.apple.com/library/archive/qa/qa1908/_index.html
archived_at: '2026-07-18T02:35:39.063188Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1908

# Finding and Fixing Category Method Name Clashes

## Q:  How can I make sure that the methods in a category don't clash with methods in the original class?

A: Categories in Objective-C allow you to add your own methods to existing classes. A category can be declared for any class, even if you don’t have the original implementation source code. Any methods that you declare in a category will be available to all instances of the original class, as well as any subclasses of the original class. At runtime, there’s no difference between a method added by a category and one that is implemented by the original class. The [Programming with Objective-C](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/ProgrammingWithObjectiveC/CustomizingExistingClasses/CustomizingExistingClasses.html) guide discusses creating your own categories.

When using a category to add methods to a class you don't control (such as the standard Cocoa or Cocoa Touch classes), you need to be very careful about method names. If the name of a method declared in a category is the same as a method in the original class, or a method in another category on the same class (or even a superclass), the behavior is undefined as to which method implementation is used at runtime. This often leads to subtle bugs or crashes which can be extremely difficult to track down. You should follow the steps listed under [Finding Category Method Name Clashes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytmobshewugsbrfvdestse) before shipping your application, to find these bugs before your customers do.

It is not possible to tell whether a given method name will conflict with an existing method defined by the original class because classes often contain private methods that are not listed in the classes interface. Further, a future version of the class may add new methods that clash with methods previously defined in your category. In order to avoid undefined behavior, it’s best practice to add a prefix to method names in categories on framework classes, just like you should add a prefix to the names of your own classes. You might choose to use the same three letters you use for your class prefixes, but lowercase to follow the usual convention for method names, then an underscore, before the rest of the method name.

__Listing 1__  Example category declaration containing a method with a prefixed name.

```objc
@interface UIView (MyCategory)

// CORRECT: The method name is prefixed.
- (BOOL)wxyz_isOccludedByView:(UIView*)otherView;

// INCORRECT: The method name is not prefixed. This method may clash with an existing method in UIView.
- (BOOL)isOccludedByView:(UIView*)otherView;

@end
```


You can use the `OBJC_PRINT_REPLACED_METHODS` environment variable to enable extra debug logging that prints a message when methods are replaced by category implementations. When a category is loaded, a message similar to Listing 2 is printed for each method in the category that clashes with an existing method in the original class.

__Listing 2__  Log output when a method is replaced by a category implementation

```
objc[21184]: REPLACED: -[UIView isOccludedByView:] by category MyCategory (IMP was 0x1873728a0 (/System/Library/Frameworks/UIKit.framework/UIKit), now 0x10002e700 (/var/mobile/Containers/Bundle/Application/14AFE8C4-EA96-4A51-8D40-F1DAD35CC3D8/<YourApplicationName>.app/<YourApplicationName>))
```

You can use the [Scheme Editor](https://developer.apple.com/library/ios/recipes/xcode_help-scheme_editor/Articles/SchemeDialog.html) to configure environment variables for your application when you run it in Xcode.

1. From the Scheme toolbar menu, choose a scheme.
2. From the same menu, choose Edit Scheme to display the scheme dialog.
3. In the left column, select Run.
4. To specify environment variables, click Environment Variables and then click the Add button.
5. Name the new environment variable `OBJC_PRINT_REPLACED_METHODS` and give it a value of `YES`.
6. Click Close.
7. Click the Run button or choose Product > Run.

__Figure 1__  You can specify arguments passed on launch and environment variables.

!!

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-03-23 | New document that describes how to use the OBJC_PRINT_REPLACED_METHODS environment variable to find category method name clashes. |

