---
title: A helper for working with temporary files in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2018/03/temp-file-helper/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:de0058eb69120ff5'
translated: false
---

> 原文：[A helper for working with temporary files in Swift](https://oleb.net/blog/2018/03/temp-file-helper/)　·　Ole Begemann

# A helper for working with temporary files in Swift

I often find myself having to create a temporary file in code for some operation, and every time it turns into a small nuisance: I have to find a suitable temp directory, make sure I give the file a unique name, and must not forget to delete the file after I’m done with it.

Actually, “create” is the wrong word because usually the API I’m using will take care of _creating_ the file — I’m just supposed to provide a URL pointing to the desired location on disk. As an example, imagine your app provides the option to share a report as a PDF file. You’d probably create a [`UIGraphicsPDFRenderer`](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer) to render the PDF and then call the [`writePDF`](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer/1649119-writepdf) method, passing in a URL to a temporary file that you plan to hand off to the iOS share sheet.

I recently wrote a small Swift helper to make this task easier. You can use it as follows.

1. Instantiate a `TemporaryFile` value with a filename of your choice:

  ```
  let tmp = try TemporaryFile(creatingTempDirectoryForFilename: "report.pdf")
  ```

  This creates a new unique temporary directory. Note that the directory is empty — as I mentioned, `TemporaryFile` doesn’t create the file for you. Rather, it provides a directory where you can safely create as many files as you want without having to worry about naming conflicts.
2. `TemporaryFile` has two properties. `directoryURL` is the URL of the temp directory it created. `fileURL` is the URL of a file in that directory, with the name you specified in the initializer:

  ```
  print(tmp.directoryURL.path)
  // → /var/folders/v8/tft1q…/T/…-8DC6DD131DC1
  print(tmp.fileURL.path)
  // → /var/folders/v8/tft1q…/T/…-8DC6DD131DC1/report.pdf
  ```

  Once again, note that the file doesn’t exist yet — it’s your job to create it, usually by passing the URL to another API that produces the output:

  ```
  let renderer = UIGraphicsPDFRenderer(...)
  try renderer.writePDF(to: tmp.fileURL) { context in
      // Drawing code
      // ...
  }
  ```

  You’re free to create more files with other names in the directory, but the `TemporaryFile` type is currently only designed to store a single file URL. It would be a nice enhancement to give it an array of additional file URLs.
3. After creating the file, the `TemporaryFile` value is designed to be passed around in your app to the object that is supposed to use the file (e.g. the caller of the function that created the file). When that object is done and the file is no longer needed, it can call the `deleteDirectory` method to delete the temporary directory, including all files in it:

  ```
  // E.g. pass temp file to UIActivityController for sharing
  // ...
  // When you're done, call deleteDirectory
  try tmp.deleteDirectory()
  ```

  I considered automating this step — you could make `TemporaryFile` a class and call `deleteDirectory` in its deinitializer. I decided against it because the behavior might be surprising to a user of the type. Adding the ability to configure the deletion behavior via an initializer flag would be another nice enhancement.

# The code

Here’s the full code (Swift 4.0):

```
import Foundation

/// A wrapper around a temporary file in a temporary directory. The directory
/// has been especially created for the file, so it's safe to delete when you're
/// done working with the file.
///
/// Call `deleteDirectory` when you no longer need the file.
struct TemporaryFile {
    let directoryURL: URL
    let fileURL: URL
    /// Deletes the temporary directory and all files in it.
    let deleteDirectory: () throws -> Void

    /// Creates a temporary directory with a unique name and initializes the
    /// receiver with a `fileURL` representing a file named `filename` in that
    /// directory.
    ///
    /// - Note: This doesn't create the file!
    init(creatingTempDirectoryForFilename filename: String) throws {
        let (directory, deleteDirectory) = try FileManager.default
            .urlForUniqueTemporaryDirectory()
        self.directoryURL = directory
        self.fileURL = directory.appendingPathComponent(filename)
        self.deleteDirectory = deleteDirectory
    }
}

extension FileManager {
    /// Creates a temporary directory with a unique name and returns its URL.
    ///
    /// - Returns: A tuple of the directory's URL and a delete function.
    ///   Call the function to delete the directory after you're done with it.
    ///
    /// - Note: You should not rely on the existence of the temporary directory
    ///   after the app is exited.
    func urlForUniqueTemporaryDirectory(preferredName: String? = nil) throws
        -> (url: URL, deleteDirectory: () throws -> Void)
    {
        let basename = preferredName ?? UUID().uuidString

        var counter = 0
        var createdSubdirectory: URL? = nil
        repeat {
            do {
                let subdirName = counter == 0 ? basename : "\(basename)-\(counter)"
                let subdirectory = temporaryDirectory
                    .appendingPathComponent(subdirName, isDirectory: true)
                try createDirectory(at: subdirectory, withIntermediateDirectories: false)
                createdSubdirectory = subdirectory
            } catch CocoaError.fileWriteFileExists {
                // Catch file exists error and try again with another name.
                // Other errors propagate to the caller.
                counter += 1
            }
        } while createdSubdirectory == nil

        let directory = createdSubdirectory!
        let deleteDirectory: () throws -> Void = {
            try self.removeItem(at: directory)
        }
        return (directory, deleteDirectory)
    }
}
```
