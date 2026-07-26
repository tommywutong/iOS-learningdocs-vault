---
title: 'prepareThumbnail(of:completionHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/preparethumbnail(of:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/preparethumbnail(of:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/preparethumbnail%28of%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:71bfc1fcb6f49320'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# prepareThumbnail(of:completionHandler:)

<sub>Instance Method</sub>

Creates a thumbnail image at the specified size asynchronously on a background thread.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepareThumbnail(of size: CGSize, completionHandler: @escaping @Sendable (UIImage?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func byPreparingThumbnail(ofSize size: CGSize) async -> UIImage?
```

## Parameters

- `size` — The desired size of the thumbnail.

- `completionHandler` — The completion handler to call when the thumbnail is ready. The handler executes on a background thread. The completion handler takes the following parameters: - **`thumbnail`** — A new thumbnail image. This parameter is `nil` if the original image isn’t backed by a [CGImage](../../coregraphics/cgimage.md) or if the image data is corrupt or malformed.

## Discussion

When displaying an image in a [UIImageView](../uiimageview.md), you can use the view’s [contentMode](../uiview/contentmode-swift.property.md) property to clip or scale the image automatically. But when the native image size is much larger than the bounds of the view, decoding the full size image creates unnecessary memory overhead. By creating a thumbnail image at a specified size with this method, you avoid the overhead of decoding the image at its full size.

This method asynchronously creates the thumbnail image on a background thread and calls the completion handler on that thread. If your app updates the UI in the completion handler, schedule the UI update on the main thread.

**Swift**

```swift
func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
    guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: cellIdentifier, for: indexPath) as? ItemCell else {
        fatalError("Unexpected type for cell. Check configuration.")
    }
        
    let item = items[indexPath.item]
    cell.nameLabel?.text = item.name
    item.image.prepareThumbnail(of: thumbnailSize) { thumbnail in
        DispatchQueue.main.async {
            cell.thumbnailImageView?.image = thumbnail
        }
    }
    return cell
}
```

**Objective-C**

```objc
- (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath {
    UICollectionViewCell *cell = [collectionView dequeueReusableCellWithReuseIdentifier:self.cellIdentifier forIndexPath:indexPath];
    NSAssert([cell isKindOfClass:[ItemCell class]], @"Unexpected type for cell. Check configuration.\n");
    
    Item *item = self.items[indexPath.row];
    ItemCell *itemCell = (ItemCell *)cell;
    itemCell.nameLabel.text = item.name;
    [item.image prepareThumbnailOfSize:self.thumbnailSize completionHandler:^(UIImage *thumbnail) {
        dispatch_async(dispatch_get_main_queue(), ^{
            itemCell.thumbnailImageView.image = thumbnail;
        });
    }];
    return cell;
}
```

## See Also

### Loading images for display

- [- imageByPreparingForDisplay](<preparingfordisplay().md>) — Decodes an image synchronously and provides a new one for display in views and animations.
- [- prepareForDisplayWithCompletionHandler:](<preparefordisplay(completionhandler_).md>) — Decodes an image asynchronously and provides a new one for display in views and animations.
- [- imageByPreparingThumbnailOfSize:](<preparingthumbnail(of_).md>) — Returns a new thumbnail image at the specified size.
