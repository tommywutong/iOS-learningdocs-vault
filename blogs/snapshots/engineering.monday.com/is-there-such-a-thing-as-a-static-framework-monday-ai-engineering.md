---
title: Is there such a thing as a static framework? - monday AI engineering
source_url: 'https://engineering.monday.com/is-there-such-a-thing-as-a-static-framework/'
source_domain: engineering.monday.com
source_group: single-site
original_language: en
published: 2021-03-25
archived_at: 2026-07-27
content_hash: 'sha256:a21fa4dd588556ed'
plan_ref: 第七周：编译、链接、Mach-O、dyld 与 App 启动 / Day 3｜静态/动态不是文件后缀问答（对应 W1-09）
plan_week: 第七周：编译、链接、Mach-O、dyld 与 App 启动
plan_day: Day 3｜静态/动态不是文件后缀问答（对应 W1-09）
container: //main
container_source: guess
---

> 原文：[Is there such a thing as a static framework? - monday AI engineering](https://engineering.monday.com/is-there-such-a-thing-as-a-static-framework/)

![Is there such a thing as a static framework?](https://engineering.monday.com/wp-content/uploads/2021/03/Static-framework-1024x599.jpg)

Mobile

# Is there such a thing as a static framework?

![Jean-David Peirolo](https://secure.gravatar.com/avatar/a2ae5ddcf5cef83720a154c905a85f503290c40656f052f76611c2871a1217d0?s=120&d=mm&r=g)

At Apple support they seem quite definitive on the topic: There is no such thing as a [“static framework”](https://developer.apple.com/forums/thread/105062). On the other hand, the internet is full of discussions that compare static vs dynamic frameworks. This posts tries to resolve the ambiguity by considering two concepts: Bundle programming, a macOS and iOS technology, and dynamic vs static linking, a more generic concept in computer science.

### A type of bundle

A framework might have a different meaning depending on how you look at it. From a Swift developer point of view, a framework is a module, which is a reusable piece of code that one can access via an import statement. From an Xcode perspective, a framework is one of the available product for targets, along with applications, plugins and libraries.

Both views offer some truth about frameworks but at the simplest, a framework is a hierarchical directory with platform specific content. Apple uses another name for this kind of structured folder, that is a bundle. A framework is one type of bundle. Other types of bundles include the Application bundle and the Plug-ins bundle. Unlike an application bundle (.app file), a framework bundle is not a package, it doesn’t appear as an opaque file to the user but as a regular directory file. This is an invite for the framework’s consumer to check its content.

Let us peek inside the [YPImagePicker](https://github.com/Yummypets/YPImagePicker) open source framework:

![](https://engineering.monday.com/wp-content/uploads/2021/03/1lWh0QPT6FTdRR1HHgre8Bg-1024x319.png)

<sub>YPImagePicker Framework</sub>

We can see what problem a framework solve. It bundles together an executable and the resources (such as images, localized strings, xibs) it depends on, making the all entity easy to share and reuse.

### Let us inspect the executable

MacOS and iOS uses the Mach-O executable format for their binaries. Mach-O binaries can be of several types: executable, archive or dynamically shared library.

The file command provides us with information on the binary Mach-O type.

![](https://engineering.monday.com/wp-content/uploads/2021/03/19XaXFiuJ-u5ewhG5EminPQ-1024x166.png)

<sub>file YPImagePicker</sub>

The YPImagePicker framework includes a dynamically linked shared library file, or dynamic library. The dynamic framework tag seems indeed appropriate in this case. (In fact, the binary stacks four different architectures into one file. This used to be an easy way to ship one binary and let the developers strip unwanted architectures in the build process. xcFramework makes this system obsolete.)

Not all frameworks include dynamic libraries. Let us now peek inside the [GoogleSignIn](https://developers.google.com/identity/sign-in/ios/sdk#download_the_google_sign-in_sdk) framework:

![](https://engineering.monday.com/wp-content/uploads/2021/03/1AMTEAcQU1PTph-WWeAWW8Q-1024x168.png)

<sub>GoogleSignIn Framework</sub>

And run the file command on the binary:

![](https://engineering.monday.com/wp-content/uploads/2021/03/1QZByRt7XImjHFq1ZACH0ew-2-1024x145.png)

<sub>file GoogleSignIn</sub>

The GoogleSignIn framework includes an archive, or static library, which is a convenient way to package multiple relocatable object files.

There is nothing exceptional in having a framework host a static library. Go over the build settings of your Xcode project and check the Mach-O type setting:

![](https://engineering.monday.com/wp-content/uploads/2021/03/1KZcNErrc9cOXmCY7juJ34Q-1024x347.png)

As expected, the default Mach-O type for a Framework project is Dynamic Library, for a Static Libary project is Static Library and for an Application project is Executable. But you are free to edit it.

### The Xcode archive

Some frameworks encapsulate dynamic libraries, others static libraries. It seems therefore natural to call the former dynamic frameworks and the latter static frameworks. However there is a fundamental difference in how dynamic frameworks are consumed.

Dynamic frameworks and their dynamically shared libraries are not fully linked into the application executable at the end of the build process. As such, they need to be embedded into the application bundle. On the contrary, once the static linker is done, all symbols have been resolved. Text and data sections have been merged into one self-sufficient executable.

![](https://engineering.monday.com/wp-content/uploads/2021/03/18z6FVkilMoMo3cJiqUCN8g-1024x292.png)

The output of the Xcode build process is an Xcode archive (a type of package specific to macOS and iOS, not to be confused with a static archive!). If we were to Xcode archive an app with the framework setup as shown in the above picture, we would get an application bundle with this configuration:

![](https://engineering.monday.com/wp-content/uploads/2021/03/1Ayou6Pdw9lVVTnO_ISVXiA.png)

The application bundle includes the MyApp executable along with frameworks that were embedded into the app, all residing in the Frameworks folder. But the application bundle doesn’t keep any trace of the non-embedded frameworks, the frameworks hosting static libraries. The GoogleSignIn executable is now part of the MyApp executable.

### Accessing Resources

If frameworks are a convenient way to ship source code with the resources it depends on, then Apple has probably made it easy to access those resources from the source code. And they did! As a type of bundle, frameworks can use the Bundle class of the Foundation utility to access their content without worrying about the underlying structure.

Consider setting an image view’s image where the source code and the resource itself are part of the framework:

```
public class MyView {
    let imageView = UIImageView()
    
    func setImage() {
        let frameworkBundle = Bundle(identifier: "com.myframework")
        let image = UIImage(named: "my_image", in: frameworkBundle, with: nil)
        imageView.image = image
    }
}
```

This code works fine in the case of a dynamic framework embedded in an application bundle. But would the framework executable be statically linked, it would crash. Indeed, in the latter case, the framework compiled source is already part of the app executable, the framework bundle is not embedded in the application bundle, so the frameworkBundle variable at line 5 returns nil at runtime.

One way to partially fix the issue uses another initializer of the Bundle class:

```
private class BundleFinder {}

public class MyView {
    let imageView = UIImageView()

    func setImage() {
        let frameworkBundle = Bundle(for: BundleFinder.self)
        let image = UIImage(named: "my_image", in: frameworkBundle, with: nil)
        imageView.image = image
    }
}
```

Here we assume that the source code and the resource will sit together. This is always true for a dynamic, embedded framework. But it requires an additional step for the consumer of a static framework. One should copy the framework’s resources into the main application bundle. That is the reason why static framework that relies on resources often comes with specific resource bundles.

Even though frameworks can host statically linked binaries, their bundle won’t be part of the final application bundle. The source code can’t assume resources are part of the framework’s bundle, which is one of the main “raison d’etre” of frameworks. Static frameworks try to merge two concepts but at the end of the road, the static linking takes precedence over the framework.
