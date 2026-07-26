---
title: 'relinquishPresentedItem(toWriter:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfilepresenter/relinquishpresenteditem(towriter:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfilepresenter/relinquishpresenteditem(towriter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfilepresenter/relinquishpresenteditem%28towriter%3A%29.json'
content_hash: 'sha256:e7b2ab457f567859'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFilePresenter](../nsfilepresenter.md)

# relinquishPresentedItem(toWriter:)

<sub>Instance Method</sub>

Notifies your object that another object or process wants to write to the presented file or directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func relinquishPresentedItem(toWriter writer: @escaping @Sendable ((@Sendable () -> Void)?) -> Void)
```

## Parameters

- `writer` — A [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) that takes another block as a parameter and returns no value. The `reacquirer` block is one you pass to the `writer` block so that your object can be notified when the `writer` is done. If your object does not need to be notified, it can pass `nil` for the `reacquirer` block.

## Discussion

You use this method to provide an appropriate response when another object wants to write to your presented URL. For example, when this method is called, you would likely stop making changes to the file or directory. After taking any appropriate steps, you must execute the block in the `writer` parameter to let the waiting object know that it may now proceed with its task. If you want to be notified when the writer has completed its task, pass your own block to the writer and use that block to reacquire the file or URL for your own uses.

> [!important] Important
> If you implement this method, you must execute the block in the `writer` parameter at the end of your implementation. The system waits for you to execute that block before allowing the `writer` to operate on the file. Therefore, failure to execute the block could stall threads in your application or other processes.

If the writer changes the file or directory, you do not need to incorporate those changes in your reacquirer block. Instead, implement the [- presentedItemDidChange](<presenteditemdidchange().md>) method and use it to detect when a writer actually wrote its changes to disk.

The following listing shows a simple implementation of this method that sets a Boolean flag that the file being monitored is not writable at the moment. After setting the flag, it executes the writer block and passes in yet another block for the writer to execute when it is done.

```objc
- (void)relinquishPresentedItemToWriter:(void (^)(void (^reacquirer)(void))) writer
{
    // Prepare for another object to write to the file.
   self.fileIsWritable = NO;
 
   // Now let the writer know that it can have the file.
   // But pass a reacquisition block so that this object
   // can update itself when the writer is done.
   writer(^{
      self.fileIsWritable = YES;
   });
}
```

Your implementation of this method is executed using the queue in the [presentedItemOperationQueue](presenteditemoperationqueue.md) property. Your reacquirer block is executed on the queue associated with the writer.

## See Also

### Related Documentation

- [- presentedItemDidChange](<presenteditemdidchange().md>) — Tells your object that the presented item’s contents or attributes changed.

### Relinquishing Managed Files

- [- relinquishPresentedItemToReader:](<relinquishpresenteditem(toreader_).md>) — Notifies your object that another object or process wants to read the presented file or directory.
