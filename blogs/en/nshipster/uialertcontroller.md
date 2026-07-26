---
title: UIAlertController
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/uialertcontroller/'
original_language: en
published: 2014-09-30
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:1759d21d874d7f07'
translated: false
---

> 原文：[UIAlertController](https://nshipster.com/uialertcontroller/)　·　NSHipster (Mattt)

# [UIAlert​Controller](https://nshipster.com/uialertcontroller/)

Written by  [Mattt](https://nshipster.com/authors/mattt/)  September 30^th, 2014

Did you know that `UIAlertView` and `UIActionSheet` (as well as their respective delegate protocols) are deprecated in iOS 8?

It’s true. ⌘-click on `UIAlertView` or `UIActionSheet` in your code, and check out the top-level comment:

> `UIAlertView` is deprecated. Use `UIAlertController` with a `preferredStyle` of `UIAlertControllerStyleAlert` instead.

Wondering why Xcode didn’t alert you to this change? Just read down to the next line:

```
@availability(iOS, introduced=2.0)
```

Although these classes are technically deprecated, this is not communicated in the `@availability` attribute. This should be of little surprise, though; `UIAlertView` has always played it fast and loose.

From its very inception, `UIAlertView` has been laden with vulgar concessions, sacrificing formality and correctness for the whims of an eager developer audience. Its `delegate` protocol conformance was commented out of its initializer (`delegate:(id /* <UIAlertViewDelegate> */)delegate`). And what protocol methods that did exist triggered when a `buttonAtIndex:` “clicked” rather than “tapped”. This, and trailing variable-length arguments for `otherButtonTitles`, awkward management of button indexes, a `-show` method with no regard for the view hierarchy… the list goes on.

`UIActionSheet` was nearly as bad, though developers can’t be bothered to remember what the heck that control is called half the time, much less complain about its awkward parts.

As such, the introduction of `UIAlertController` should be met like an army liberating a city from occupation. Not only does it improve on the miserable APIs of its predecessors, but it carves a path forward to deal with the UIKit interface singularity brought on by the latest class of devices.

This week’s article takes a look at `UIAlertController`, showing first how to port existing alert behavior, and then how this behavior can be extended.

---

`UIAlertController` replaces both `UIAlertView` and `UIActionSheet`, thereby unifying the concept of alerts across the system, whether presented modally or in a popover.

Unlike the classes it replaces, `UIAlertController` is a subclass of `UIViewController`. As such, alerts now benefit from the configurable functionality provided with view controller presentation.

`UIAlertController` is initialized with a `title`, `message`, and whether it prefers to be displayed as an alert or action sheet. Alert views are presented modally in the center of their presenting view controllers, whereas action sheets are anchored to the bottom. Alerts can have both buttons and text fields, while action sheets only support buttons.

Rather than specifying all of an alert’s buttons in an initializer, instances of a new class, `UIAlertAction`, are added after the fact. Refactoring the API in this way allows for greater control over the number, type, and order of buttons. It also does away with the delegate pattern favored by `UIAlertView` & `UIActionSheet` in favor of much more convenient completion handlers.

## Comparing the Old and New Ways to Alerts

### A Standard Alert

![A Standard Alert](https://nshipster.com/assets/uialertcontroller-alert-defautl-style-3fbfc10a51183c4a7eab291a3e3a18a1a6d9ac42b49dacb9c0ec53fca6eeabd93ea054cd54ac86ab9af9d2f3cd84ee8a1be6b154aa0e7725df5f22d58a46a477.png)

#### The Old Way: UIAlertView

```
let alertView = UIAlertView(title: "Default Style", message: "A standard alert.", delegate: self, cancelButtonTitle: "Cancel", otherButtonTitles: "OK")
alertView.alertViewStyle = .Default
alertView.show()

// MARK: UIAlertViewDelegate

func alertView(alertView: UIAlertView, clickedButtonAtIndex buttonIndex: Int) {
    switch buttonIndex {
        …
    }
}
```

#### The New Way: UIAlertController

```
let alertController = UIAlertController(title: "Default Style", message: "A standard alert.", preferredStyle: .Alert)

let cancelAction = UIAlertAction(title: "Cancel", style: .Cancel) { (action) in
    …
}
alertController.addAction(cancelAction)

let OKAction = UIAlertAction(title: "OK", style: .Default) { (action) in
    …
}
alertController.addAction(OKAction)

self.presentViewController(alertController, animated: true) {
    …
}
```

### A Standard Action Sheet

![A Standard Action Sheet](https://nshipster.com/assets/uialertcontroller-action-sheet-automatic-style-0daf5f151d1b2b5381ccbd7f09421b34be9e96b65879b885007d6535df34967615369c15d61d5f987779718ef18e107e1a50015241f29d444645fe7a6dd90f98.png)

#### UIActionSheet

```
let actionSheet = UIActionSheet(title: "Takes the appearance of the bottom bar if specified; otherwise, same as UIActionSheetStyleDefault.", delegate: self, cancelButtonTitle: "Cancel", destructiveButtonTitle: "Destroy", otherButtonTitles: "OK")
actionSheet.actionSheetStyle = .Default
actionSheet.showInView(self.view)

// MARK: UIActionSheetDelegate

func actionSheet(actionSheet: UIActionSheet, clickedButtonAtIndex buttonIndex: Int) {
    switch buttonIndex {
        ...
    }
}
```

#### UIAlertController

```
let alertController = UIAlertController(title: nil, message: "Takes the appearance of the bottom bar if specified; otherwise, same as UIActionSheetStyleDefault.", preferredStyle: .ActionSheet)

let cancelAction = UIAlertAction(title: "Cancel", style: .Cancel) { (action) in
    …
}
alertController.addAction(cancelAction)

let OKAction = UIAlertAction(title: "OK", style: .Default) { (action) in
    …
}
alertController.addAction(OKAction)

let destroyAction = UIAlertAction(title: "Destroy", style: .Destructive) { (action) in
    println(action)
}
alertController.addAction(destroyAction)

self.presentViewController(alertController, animated: true) {
    …
}
```

## New Functionality

`UIAlertController` is not just a cleanup of pre-existing APIs, it’s a generalization of them. Previously, one was constrained to whatever presets were provided (swizzling in additional functionality at their own risk). With `UIAlertController`, it’s possible to do a lot more out-of-the-box:

### Alert with Destructive Button

![Alert with Destructive Button](https://nshipster.com/assets/uialertcontroller-alert-cancel-destroy-63ddefecf1cbbd15e32c85c70ae8a548a6381f356d69780e65c9062599896ea56cbde4b0b519319c945e217dddbedf097aad55a178b90f5c7b420bbb64585198.png)

The type of an action is specified by `UIAlertActionStyle`, which has three values:

> - `.Default`: Apply the default style to the action’s button.
> - `.Cancel`: Apply a style that indicates the action cancels the operation and leaves things unchanged.
> - `.Destructive`: Apply a style that indicates the action might change or delete data.

So, to add a destructive action to a modal alert, just add a `UIAlertAction` with style `.Destructive`:

```
let alertController = UIAlertController(title: "Title", message: "Message", preferredStyle: .Alert)

let cancelAction = UIAlertAction(title: "Cancel", style: .Cancel) { (action) in
    println(action)
}
alertController.addAction(cancelAction)

let destroyAction = UIAlertAction(title: "Destroy", style: .Destructive) { (action) in
    println(action)
}
alertController.addAction(destroyAction)

self.presentViewController(alertController, animated: true) {
    …
}
```

### Alert with \>2 Buttons

![Alert with More Than 2 Buttons](https://nshipster.com/assets/uialertcontroller-alert-one-two-three-cancel-46c302528712f0a7472d4b915d3db974d725d7f171470988a56236db04f56e07d020ad601ae80aa7fc7cce67aa7ba0e8fa8970715ad8b936325850a6a125c7ae.png)

With one or two actions, buttons in an alert are stacked horizontally. Any more than that, though, and it takes on a display characteristic closer to an action sheet:

```
let oneAction = UIAlertAction(title: "One", style: .Default) { (_) in }
let twoAction = UIAlertAction(title: "Two", style: .Default) { (_) in }
let threeAction = UIAlertAction(title: "Three", style: .Default) { (_) in }
let cancelAction = UIAlertAction(title: "Cancel", style: .Cancel) { (_) in }

alertController.addAction(oneAction)
alertController.addAction(twoAction)
alertController.addAction(threeAction)
alertController.addAction(cancelAction)
```

### Creating a Login Form

![Creating a Login Form](https://nshipster.com/assets/uialertcontroller-alert-username-password-login-forgot-password-cancel-aae008cebfe988b693dfe17bc77a26614011d27240c28f4c0447ff6f304fa90599f91e8db39c330e875837d60cd15132d6d152425ba7d5972c5da6af70fa6e47.png)

iOS 5 added the `alertViewStyle` property to `UIAlertView`, which exposed much sought-after private APIs that allowed login and password fields to be displayed in an alert, as seen in several built-in system apps.

In iOS 8, `UIAlertController` can add text fields with the `addTextFieldWithConfigurationHandler` method:

```
let loginAction = UIAlertAction(title: "Login", style: .Default) { (_) in
    let loginTextField = alertController.textFields![0] as UITextField
    let passwordTextField = alertController.textFields![1] as UITextField

    login(loginTextField.text, passwordTextField.text)
}
loginAction.enabled = false

let forgotPasswordAction = UIAlertAction(title: "Forgot Password", style: .Destructive) { (_) in }
let cancelAction = UIAlertAction(title: "Cancel", style: .Cancel) { (_) in }

alertController.addTextFieldWithConfigurationHandler { (textField) in
    textField.placeholder = "Login"

    NSNotificationCenter.defaultCenter().addObserverForName(UITextFieldTextDidChangeNotification, object: textField, queue: NSOperationQueue.mainQueue()) { (notification) in
        loginAction.enabled = textField.text != ""
    }
}

alertController.addTextFieldWithConfigurationHandler { (textField) in
    textField.placeholder = "Password"
    textField.secureTextEntry = true
}

alertController.addAction(loginAction)
alertController.addAction(forgotPasswordAction)
alertController.addAction(cancelAction)
```

### Creating a Sign Up Form

![Creating a Sign Up Form](https://nshipster.com/assets/uialertcontroller-alert-sign-up-e54bae1d3d0a202a222e152f1a149c17124b7a0c5a2febbeb65f54cd958d22efb13ff1f0aecb45f9452fc7350d9a2d6ad2bd55e7e932ce2d3b1c5858bd04ca62.png)

`UIAlertController` goes even further to allow any number of text fields, each with the ability to be configured and customized as necessary. This makes it possible to create a fully-functional signup form in a single modal alert:

```
alertController.addTextFieldWithConfigurationHandler { (textField) in
    textField.placeholder = "Email"
    textField.keyboardType = .EmailAddress
}

alertController.addTextFieldWithConfigurationHandler { (textField) in
    textField.placeholder = "Password"
    textField.secureTextEntry = true
}

alertController.addTextFieldWithConfigurationHandler { (textField) in
    textField.placeholder = "Password Confirmation"
    textField.secureTextEntry = true
}
```

Though, it must be said, _caveat implementor_. Just because you _can_ implement a signup form in an alert doesn’t mean you _should_. Suck it up and use a view controller, like you’re supposed to.

## Caveats

Attempting to add a text field to an alert controller with style `.ActionSheet` will throw the following exception:

> Terminating app due to uncaught exception `NSInternalInconsistencyException`, reason: ‘Text fields can only be added to an alert controller of style `UIAlertControllerStyleAlert`’

Likewise, attempting to add more than one `.Cancel` action to either an alert or action sheet will raise:

> Terminating app due to uncaught exception `NSInternalInconsistencyException`, reason: ‘`UIAlertController` can only have one action with a style of `UIAlertActionStyleCancel`’
