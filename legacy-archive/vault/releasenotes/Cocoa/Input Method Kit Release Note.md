---
title: Input Method Kit Release Note
apple_id: TP40004740
resource_type: Release Note
platform: macOS
topic: User Experience
technology: InputMethodKit
published: '2007-07-17'
source_url: https://developer.apple.com/library/archive/releasenotes/Cocoa/RN-InputMethodKit/index.html
archived_at: '2026-07-18T02:50:22.694874Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Input Method Kit Release Note for OS X v10.5

The Input Method Kit (`/System/Library/InputMethodKit.framework`) is a new Objective-C framework for building input methods for Chinese, Japanese, and other languages. This framework handles connecting to clients, running candidate windows, and various other tasks that, in the past, you needed to provide code for. By using the Input Method Kit, you are free to focus exclusively on developing the core functionality of your input method product—the text conversion engine.

The support provided by the Input Method Kit is fairly simple. It uses just two, or optionally three, classes. You must use the `IMKServer` and the `IMKInputController` class. If you want to use candidate windows, you also need to use the `IMKCandidates` class.

#### Contents:

- [How the Input Method Kit Works](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donbqfvcg63tujruw422fnrsw2zlooreuixzr)
- [For More Information](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2donbqfvcg63tujruw422fnrsw2zlooreuixzs)

### How the Input Method Kit Works

Every input method creates an `IMKServer` object in its main function. One of the parameters for the `IMKServer` object is a connection name. The `IMKServer` object uses this name to create an `NSConnection` object that clients use to connect to the input method. The only client in OS X v10.5 is the Text Services Manager.

When a client requests an input session, the `IMKServer` object allocates an `IMKInputController` object or a class that inherits from `IMKInputController`. This object then receives input from that client session. Note that `IMKServer` creates a controller object for each session request. This frees you from the need to manage sessions; the `IMKServer` object manages them for you. When a controller method is called, it is always from the same session.

You have several options for handling input from clients, each of which is discussed further in the `IMKInputController.h` header file. The simplest approach is to write a delegate class that implements one of the methods for receiving input.

Another approach is to create a delegate class that handles input. Then you override `IMKInputController` to take advantage of the utilities provided by that class.

### For More Information

For more information see:

- These reference documents: [IMKCandidates Class Reference](https://developer.apple.com/documentation/inputmethodkit/imkcandidates), [IMKInputController Class Reference](https://developer.apple.com/documentation/inputmethodkit/imkinputcontroller), [IMKServer Class Reference](https://developer.apple.com/documentation/inputmethodkit/imkserver), [IMKMouseHandling Protocol Reference](https://developer.apple.com/documentation/inputmethodkit/imkmousehandling), IMKServerInput Protocol Reference, [IMKStateSetting Protocol Reference](https://developer.apple.com/documentation/inputmethodkit/imkstatesetting), and IMKTextInput Protocol Reference.
- The documentation that is included with the _[BasicInputMethod](../../samplecode/BasicInputMethod/BasicInputMethod.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanrwgi)_ and _InputMethods_ sample code.
