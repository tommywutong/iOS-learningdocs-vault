---
title: The Amazing Responder Chain
source_url: 'https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/'
source_domain: cocoanetics.com
source_group: single-site
original_language: en
published: 2012-09-29
archived_at: 2026-07-27
content_hash: 'sha256:8b5caa2a96213412'
plan_ref: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期 / Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01）
plan_week: 第五周：RunLoop、AutoreleasePool、响应者链与生命周期
plan_day: Day 4｜事件先命中视图，再沿响应者链寻找处理者（对应 W4-07、W5-01）
container: '//div[@id=''content'']'
container_source: guess
---

> 原文：[The Amazing Responder Chain](https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/)

# The Amazing Responder Chain

[Sep 29, 2012](https://www.cocoanetics.com/2012/09/the-amazing-responder-chain/)

Do you remember, back when you first opened Interface Builder?

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-13.06.42.png?resize=397%2C71)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-13.06.42.png)

How long did it take you to understand the purpose of **File’s Owner**?

That is a proxy for the object that loads this NIB, usually a UIViewController. This allows you to connect IBOutlets and IBActions with elements contained in the NIB file. IB knows about these because you tell it what class the File’s Owner has and from parsing this class’ header it finds all things that you can connect to by the IBOutlet and IBAction keyword.

That one was easy. Second question: How long did it take you to understand the purpose of **First Responder**?

If you are like me then you started out developing for the iPhone and other iOS devices. And then you probably also learned to ignore this proxy object because on iOS it does not serve an obvious purpose. In fact you can go for years developing iOS apps without ever doing anything with it. I know I did.

It is only know that I am starting to dabble in developing for the Mac that I had to begin to develop and appreciation for the responder chain. And so finally I understand the purpose and usefulness of the “First Responder” object and I want to share this with you.

You might have heard about or read about the existence of this Responder Chain. The closest one usually gets to dealing with it is that you want to dismiss the keyboard of a UITextField and you do this by calling resignFirstResponder. The second run in usually is when you implement cut/copy/paste and you need to allow a UIView to canBecomeFirstResponder and then you implement cut:, copy: and paste: methods to have these show up in the UIMenuController popover.

### Why You Didn’t Use It So Far

On iOS you usually only ever have to deal with a single screen full of information. This screen, especially on iPhone, is usually contained in a single UIViewController. So you can easily get by with connecting all your actions to outlets in the File’s Owner. Seriously, why would anybody want to have an object outside of the current NIB respond to an action like a button press or copy command?

Well, on Mac the story is more complex since you can have multiple windows open at the same time. You can be working on 3 documents simultaneously. But which of these windows is now supposed to respond to the user choosing Copy in the menu? It took me about an hour to rid my head from the notion of connecting a menu item to a specific view controller and uncover how it is done differently there.

If you connect a button to an outlet this employs the target/action paradigm. The action is defined by the name of a selector. The target can either be a concrete object or it can be NULL. If you connect to File’s Owner then the target is set to the concrete instance that File’s Owner is acting as proxy for. If you do this in code you call addTarget:action:forControlEvents: achieving exactly the same.

On Mac we cannot say at design time in IB who will take care of a specific action. Hence we need to employ the awesome services of the Responder Chain.

### The Chain of Responders

You can think of the Responder Chain as a very elegant solution for answering the question “Who might be interested in this event X?”

Whenever any event occurs the system first asks the current First Responder. On iOS any UIResponder subclass can become first responder. If a text field is active and the cursor is blinking inside it to show the readiness for text input then it has first responder status. So it gets first dibs on all events.

There might be some actions however where the text fields does not know how to respond to. For these cases the system walks up this Responder Chain and keeps asking each object in this chain if it is interested in dealing with this action. Considering for example the standard action **copy:** the default is to assume that a responder wants to take care of the the copy action if such a selector exists in the responds’s implementation. This can be overridden by implementing **canPerformAction:withSender:** and responding with NO. Then the next responder will be asked.

This process of asking each responder will be done for each action and for the entire chain. A variant of this process occurs if the system wants to display a menu item (on OSX) or a popup menu (on iOS). If there is no responder willing to volunteer then the menu option will be disabled or invisible. This is quite useful because there you don’t need to implement logic to enable/disable menu options, but this is done for you. If there is a willing responder to an action then it will be enabled, otherwise disabled.

Let’s get a quick picture of how the responder chain looks on iOS and OSX.

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-14.55.58.png?resize=384%2C356)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-14.55.58.png)

Apple [explains](http://developer.apple.com/library/ios/#DOCUMENTATION/EventHandling/Conceptual/EventHandlingiPhoneOS/EventsiPhoneOS/EventsiPhoneOS.html) the rules for traveling along the chain such:

1. The **hit-test view or first responder** passes the event or message to its **view controller** if it has one; if the view doesn’t have a view controller, it passes the event or message to its superview.
2. If a view or its view controller cannot handle the event or message, it passes it to the **superview** of the view.
3. Each subsequent superview in the hierarchy follows the pattern described in the first two steps if it cannot handle the event or message.
4. The topmost view in the view hierarchy, if it doesn’t handle the event or message, passes it to the **window** object for handling.
5. The UIWindow object, if it doesn’t handle the event or message, passes it to the singleton **application** object.

As of iOS 5 there is a step 6: The app delegate gets the final word on events. Beginning with iOS 5 the **app delegate** inherits from UIResponder and no longer from NSObject as it did before.

In short: first the view, if the view has a view controller then that, next the superview until the top of the hierarchy, the window. From there to the application and finally to the app delegate.

The addition of the app delegate as potential responder is a welcome addition since we rarely – if ever – subclass UIApplication or UIWindow. But we always have _our own app delegate_ if only to create the window and add the rootViewController in the application:didFinishLaunching… delegate method. So this happens to be the de facto best place for a responder to fall back to if there is none in the entire view hierarchy.

Look at the following comparison and you can see that the concept is virtually identical on iOS (left) and Mac (right).

[![](https://i0.wp.com/www.cocoanetics.com/files/iOS_and_OSX_responder_chain_2x.png?resize=633%2C371)](https://i0.wp.com/www.cocoanetics.com/files/iOS_and_OSX_responder_chain_2x.png)

The only obvious difference here is that view controllers appear to be a relatively new concept to OS X. I presume that this is because view controllers are much less used on OS X than they are on iOS. They also load a view from a NIB. One scenario where I saw NSViewController to be used was as an accessory view in a file open dialog.

On OS X the top level control object would typically be an NSWindowController, again in charge of a window loaded from NIB. On iOS view controllers play a much more important role because container view controllers like UITabBarController or UINavigationController would work with these as a means to group views.

Long story short, at present view controllers are not part of the responder chain on Mac, but they are on iOS.

But the story does not end there if your Mac-app is document-based, because there the responder chain is extended to include multiple document-related objects as well.

[![](https://i0.wp.com/www.cocoanetics.com/files/doc_based.jpg?resize=613%2C133)](https://i0.wp.com/www.cocoanetics.com/files/doc_based.jpg)

From what I have seen so far on Mac you can go a long way without sub-classing NSApplication, NSDocumentController or even providing an app delegate. The must-subclass element in this chain is NSDocument.

Consider an **import:** action that would allow the user to import content into an open document. If there is no document window open the action should be grayed out. Of course the NSDocument sub-class would be the ideal place for the implementation as this function relates to a specific document.

### Implementing Responder-Chained Actions on Mac

As I mentioned before I was stumped at first trying to implement an import menu item for a Mac app. There you have a MainMenu.xib that has a File’s Owner class of NSApplication. So NSApplication loads the menu from NIB when the app launches. So there it wouldn’t make sense connecting actions to File’s Owner since in all likelihood you wouldn’t even have a custom NSApplication sub-class.

Instead you click on First Responder and go to the inspector tab with the Shield icon. There you can see all user-defined actions and we add an import action.

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.16.58.png?resize=630%2C339)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.16.58.png)

Now you can Ctrl-Click and drag a line from the newly inserted menu item onto First Responder.

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.20.23.png?resize=524%2C353)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.20.23.png)

In the subsequent pop up you can choose which action to connect that to. Besides of the freshly defined import you also see all the system-defined actions.

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.20.30.png?resize=254%2C255)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.20.30.png)

… and of course the other direction of connection works just as well. In the outlets tab the import selector also appears.From its circular outlet symbol you can also drag to the menu item.

Next you implement a matching action method in the document class.

```
- (void)import:(id)sender
{
   // fancy importing action
}
```

No need for an IBAction keyword instead of the void here. Contrasting to the route via File’s Owner we don’t need this hint to tell interface builder in the header which actions are available to link to.

That is all there is to it. If you have a document window open, the responder chain knows that there is somebody able to take care of the import and so the Menu Option becomes available. Conversely if you close all document windows it automatically becomes grayed out.

“Awesome service!” that’s what we call that. The best code is always the one we _don’t have to write_.

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.30.18.png?resize=182%2C282)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.30.18.png)[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.30.33.png?resize=179%2C281)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-16.30.33.png)

And now for the same stunt on iOS.

### Implementing Responder-Chained Actions on iOS

The use case for those is obviously a much rarer on iOS. As I alluded to above the main reason being that you don’t have an app-wide menu by which the user would give the majority of commands, but rather you’d have some controls laid out on a view controlled by a view controller. And this view controller would be the File’s Owner offering the outlets for connection to the controls.

There is however a scenario where knowing about this method can simplify your life. Consider the situation where you want to have an event in a subview trigger something on the application level. Flipping between two view controllers comes to mind.

The current Xcode template for a utility app employs a complicated system for achieving the flip. There is a MainViewController which has an info button which presents a FlipsideViewController. This button is linked to the view controller via File’s Owner.

Without any changes to our code we could also define a showInfo user-defined action to the MainViewController’s First Responder. Then we could link the info button to that instead of the File’s Owner. Everything still works.

Consider another example. Let’s say you have an app that has multiple view controllers that are peers. Those would be presented by a container view controller, similar to a UITabBarController. You could have a button in one of these sub-viewcontrollers, but the responding action method could be part of the container view controller.

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-17.27.20.png?resize=450%2C391)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-17.27.20.png)

There the event would travel up the responder chain. View, view controller, superview (= container’s view), container view controller and there it would find the action. Without the responder chain you would have to employ some trickery to have the button press be communicated all the way up to the container view controller.

In fact even Apple often employs delegate protocols to have a view controller communicate to its superior. For example the FlipSideViewController of the above mentioned utility app template has a protocol just for handling the Done button:

```
@protocol FlipsideViewControllerDelegate
- (void)flipsideViewControllerDidFinish:(FlipsideViewController *)controller;
@end
```

With what we know now we can easily make this delegate protocol unnecessary and instead have a flipBack action on the responder chain that achieves the same effect with much less code.

Create a flipBack: action on the First Responder and link the Done button action to that after breaking the link to File’s Owner.

[![](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-17.34.36.png?resize=588%2C282)](https://i0.wp.com/www.cocoanetics.com/files/Screen-Shot-2012-09-29-at-17.34.36.png)

Then implement the flipBack action in MainViewController.

```
- (void)flipBack:(id)sender
{
	[self dismissViewControllerAnimated:YES completion:nil];
}
```

Now we can get rid of the delegate protocol, the delegate property on FlipsideViewController and the done: action there that calls the delegate’s flipsideViewControllerDidFinish: method.

If the user taps on the Done button now the action travels: FlipsideViewController, MainViewController’s view, MainViewController and there it finds the flipBack: action to execute.

Granted, there are scenarios where you want the modally presented sub-viewcontroller communicate success or failure to its delegate. But for a simple scenario like this using the responder chain makes it much simpler.

### Bonus: Hiding the Keyboard Even Without Knowing the Current First Responder

You can also employ the responder chain mechanism for triggering actions where you don’t know or don’t care who the responder will be. Like, for example, when you want the keyboard to go away but could not be bothered to keep track of the current first responder.

The iOS keyboard shows whenever a view is first responder that implements the UIKeyInput or UITextInput protocol. If you have multiple UITextField instances on screen then you would have to keep track which currently is the first responder if you wanted to be able to dismiss the keyboard programmatically. Or alternatively I’ve been known to call resignFirstResponder on all text fields in succession because any one of them would be it.

Knowing about the responder chain allow us to dismiss the keyboard without any prior knowledge. We only would have to know how to send a message down the responder chain and we’d be guaranteed that the keyboard-producing view would be first in line.

Mac Guru Sean Heber taught us how:

> [[UIApplication sharedApplication] sendAction:@selector(resignFirstResponder) to:nil from:nil forEvent:nil];
> 
> — Sean Heber (@BigZaphod) [August 1, 2012](https://twitter.com/BigZaphod/status/230744266509516800)

Any selector can be used for the action parameter of the sendAction method that UIApplication used to message the responder chain. If the recipient is nil then it will start to travel in the responder chain, of course beginning with the First Responder. Oh and what a coincidence! This first responder is also the text field that we want to resign its status as such.

### Conclusion

The responder chain is a great concept and it simplifies Menu actions on Mac where you want the document to respond to the actions. On iOS Apple employes the very same method albeit refined with the insertion of view controllers in the chain.

Understanding how to use the responder chain to your advantage can save you a few architectural headaches and the basic knowledge presented in this article should have gotten you a long way along to a better understanding of how to use it to your advantage.

Since the app delegate has been promoted to a UIResponder as of iOS 5 there might even be some scenarios where you’d want to have the responding action located there. And then you could trigger these actions from way down your view hierarchy without having to go via the [UIApplication sharedApplication].delegate singleton. Admit it, you are guilty of doing that on more than one occasion, right?

---

**Categories:**[Recipes](https://www.cocoanetics.com/category/recipes/)

[← Fun with UTI](https://www.cocoanetics.com/2012/09/fun-with-uti/)

[Radar: First Responder defunct when used in Storyboard →](https://www.cocoanetics.com/2012/09/radar-first-responder-defunct-when-used-in-storyboard/)

### Trackbacks

1. [Radar: First Responder defunct when used in Storyboard | Cocoanetics](http://www.cocoanetics.com/2012/09/radar-first-responder-defunct-when-used-in-storyboard/)
2. [The Lion’s Full Screen Mode | Cocoanetics](http://www.cocoanetics.com/2012/11/the-lions-full-screen-mode/)
