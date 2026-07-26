---
title: Passing Data Between View Controllers
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/02/passing-data-between-view-controllers/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bd81cdfd9b1558e3'
translated: false
---

> 原文：[Passing Data Between View Controllers](https://oleb.net/blog/2012/02/passing-data-between-view-controllers/)　·　Ole Begemann

# Passing Data Between View Controllers

A very common pattern on iOS is for one view controller to react to a user action (such as tapping on a button or table cell) by creating and presenting another view controller. In code, this looks something like this:

```
- (IBAction)nextScreenButtonTapped:(id)sender
{
    DestinationViewController *destinationController = [[DestinationViewController alloc] init];
    [self.navigationController pushViewController:destinationController animated:YES];
}
```

In all but the simplest cases this code is not sufficient because we usually have to configure the new screen before we present it. The calling view controller (`self` in this context) has information that needs to be shown on the view that is to be presented by the new view controller. Let’s assume the destination view contains a text field whose text must be set. Since the text field can be accessed via a public property in `DestinationViewController`, many beginners extend the code in the most straightforward way: just set the text field’s text directly from the source view controller.

```
- (IBAction)nextScreenButtonTapped:(id)sender
{
    DestinationViewController *destinationController = [[DestinationViewController alloc] init];
    destinationController.nameTextField.text = self.myModel.name;
    [self.navigationController pushViewController:destinationController animated:YES];
}
```

# Don’t Misuse Views For Storing Data

This approach fails because at the time the line `destinationController.nameTextField.text = ...` is executed, the `DestinationViewController`’s view has not yet been loaded and therefore the text field (one of the controller’s view’s subviews) does not yet exist. `nameTextField` will be `nil` and the line of code above does nothing. Now, the easiest way to fix this is to make sure the view controller’s view gets loaded before the code is executed. You can do this by accessing the view controller’s `view` property, which automatically will attempt to load the view:

```
- (IBAction)nextScreenButtonTapped:(id)sender
{
    DestinationViewController *destinationController = [[DestinationViewController alloc] init];
    if (destinationController.view) {
        destinationController.nameTextField.text = self.myModel.name;
    }
    [self.navigationController pushViewController:destinationController animated:YES];
}
```

Now this works, but you should not do it this way. There are at least three reasons why this piece of code is bad design:

1. To people who don’t know that accessing the `view` property implicitly loads the view, this code is very obscure. Why the need for the `if (destinationController.view) { ... }` statement? The could would require an explanatory comment to make its purpose clear. If you find yourself having to add comments to simple-looking code, it is often a sign of bad design. In my opinion, the vast majority of your code should be able to explain itself without any comments.
2. It breaks encapsulation. A view controller’s view and all its subviews should only be accessed by the view controller that owns these objects. It is that view controller’s job and sole responsibility to manage its view(s), and no other object should have to interfere in this relationship. Instead, the view controller should offer a clean public interface to allow outside objects to configure it.
3. You must not use views to store data. In this example, the `nameTextField` is the only object managed by the view controller that stores the string to be edited. This is an absolute no-go. It is not only bad design in the model-view-controller context but can also potentially lead to data loss. In iOS, view controllers are expected to destroy their views under memory pressure when those views are not currently visible. If this happens to a text field that is the sole storage for an edited model property, data has been lost.

# The Solution

The solution for this problem is to declare another public property `NSString *name` in the `DestinationViewController` class and assign the data to this property first:

```
- (IBAction)nextScreenButtonTapped:(id)sender
{
    DestinationViewController *destinationController = [[DestinationViewController alloc] init];
    destinationController.name = self.myModel.name;
    [self.navigationController pushViewController:destinationController animated:YES];
}
```

Then, in `-[DestinationViewController viewDidLoad]`, we know the view (and with it our text field) has been loaded and we can assign the text to the text field:

```
- (void)viewDidLoad
{
    [super viewDidLoad];
    self.nameTextField.text = self.name;
}
```

The view controller must also take care to update its `name` property whenever the user edits the text in the text field. That way, the `name` property acts as storage for the user’s data and the view controller remains in a safe state when its view gets unloaded.

**Update February 24, 2012:** Several people have pointed out to me that there are other ways to pass data to the target view controller that in many cases might even be better. One such method is to define a custom `init...` method in the target view controller that takes the data the view controller needs as arguments. This makes the purpose of the class even clearer and does avoid possible problems when another object assign a new value to the property when the view is already on screen. In code, this would look like this:

```
- (IBAction)nextScreenButtonTapped:(id)sender
{
    DestinationViewController *destinationController = [[DestinationViewController alloc]
        initWithName:self.myModel.name];
    [self.navigationController pushViewController:destinationController animated:YES];
}
```

And in `DestinationViewController.m`:

```
// DestinationViewController.m
- (id)initWithName:(NSString *)theName
{
    self = [super initWithNibName:@"DestinationViewController" bundle:nil];
    if (self) {
        _name = [theName copy];
    }
    return self;
}

- (void)viewDidLoad
{
    [super viewDidLoad];
    self.nameTextField.text = _name;
}
```

Others proposed to declare a custom datasource protocol that `DestinationViewController` uses to obtain the data it needs from its data source (usually its parent view controller), much like `UITableView` works. This is also a good suggestion. It involves a few more lines of code but makes the coupling between the objects even looser.

Finally, several readers asked me why I opted to pass `self.myModel.name` to the destination view controller instead of passing the entire model object (`self.myModel`). Both are definitely possible. Which approach is the better one depends on the purpose of the destination view controller in my opinion. If the view controller is designed to display and/or edit all or most of the model object’s attributes, it is definitely better to pass the whole object along. On the other hand, if the view controller is a generic editing controller whose purpose is to edit an arbitrary string, you should just pass this string to it. In this case, the destination view controller should not need to know anything about the model object whose attribute it edits.

Thanks to everybody who sent in their comments.
