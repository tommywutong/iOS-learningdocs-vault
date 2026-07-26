---
title: 'Using ''swift package fetch'' in an Xcode project | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/blog/package-manager-fetch.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-26
content_hash: 'sha256:3830c3b664a5ae0d'
translated: false
---

> 原文：[Using 'swift package fetch' in an Xcode project | Cocoa with Love](https://www.cocoawithlove.com/blog/package-manager-fetch.html)　·　Cocoa with Love (Matt Gallagher)

Up until now, the Cocoa with Love git repositories have included their dependencies as “git subtrees” where each dependency is copied and statically hosted within the depender. I want to replace this arrangement with a more dynamic dependency management while remaining totally transparent to users of the library.

I’d like to use the Swift Package Manager for the task but it’s complicated by the fact that I don’t want the Swift Package Manager to be a required way to build any of these repositories. The Swift Package Manager has a very narrow range of build capabilities and I don’t want my libraries to be subject to these limitations.

In this article, I’ll look at a hybrid approach where the Swift Package Manager is used as a behind-the-scenes tool to fetch dependencies for an otherwise manually configured Xcode project that continues to support the same target platforms and build structures from the previous “subtree” arrangement.

> **Update for Xcode 10**: while this approach is tested and still works in Xcode 10, the compromises required have increased and I’ve reverted to using git subtrees for my own projects. See [Article updates, 2018 edition](https://www.cocoawithlove.com/blog/updating-for-2018.html#package-manager-fetch-deprecated) for more information.

## Managing dependencies

The dependency graph for the CwlSignal library that I released last year is pretty simple:

CwlCatchException ← CwlPreconditionTesting ← CwlUtils ← CwlSignal

### Git subtree

Until now, I’ve been using [Git subtrees](https://github.com/git/git/blob/master/contrib/subtree/git-subtree.txt).

In this arrangement, you don’t need to separately download any dependencies; if you browse [the previous structure of the CwlSignal repository](https://github.com/mattgallagher/CwlSignal/tree/72d4a10656ff4c8de8083e88f8651c5f7d0b8e47), you’ll notice that it contains [CwlUtils](https://github.com/mattgallagher/CwlSignal/tree/72d4a10656ff4c8de8083e88f8651c5f7d0b8e47/CwlUtils), which contains [CwlPreconditionTesting](https://github.com/mattgallagher/CwlSignal/tree/72d4a10656ff4c8de8083e88f8651c5f7d0b8e47/CwlUtils/CwlPreconditionTesting), which contains [CwlCatchException](https://github.com/mattgallagher/CwlSignal/tree/72d4a10656ff4c8de8083e88f8651c5f7d0b8e47/CwlUtils/CwlPreconditionTesting/CwlCatchException). This is not totally different to manually copying the files into each repository but with the minor advantage that if a dependency changes, I can easily pull changes into the depender with a simple subtree pull.

This arrangement has its problems. Subtrees scale poorly since changes need to be manually pulled into each subsequent link in the chain; you can’t easily update all dependencies with a single command. Each repository is bloated by needing to contain its dependencies. It also creates merge problems if you accidentally modify a dependency’s subtree in the depender then try to pull the dependency.

None of these are major problems for a small, simple dependency graph like CwlSignal but they’ve always been concerns that I’ve wanted to address.

### Git submodules

I could use [git submodule](https://git-scm.com/docs/git-submodule). In theory, it’s just a more dynamic approach for the problem that git subtrees solve. I feel as though git submodules should be ideal choice but in practice, git modules are not a transparent change to your git repository and their poor handling by git makes them confusing and frustrating for users.

It is possible to pull and push repositories in the wrong order and end up overwriting your changes. Switching from one dependency to another is complicated and often involves manually editing the contents of the “.git” directory. The “Download ZIP” functionality on Github becomes completely useless as the ZIP file omits the submodule references as do most other non-git means of managing your code.

In comparison to git subtrees which usually go unnoticed, submodules suffer from the fact that every user needs to be aware of the submodule arrangement and needs to run slightly different git commands just to fetch and update the repository correctly.

### Established package managers

I could move to an established package manager like [CocoaPods](https://cocoapods.org) or [Carthage](https://github.com/carthage/carthage). While I should probably do more to improve compatibility with these systems for users who _want_ to use them, I’d rather not force _everyone_ to use them. For my own purposes, I’d rather avoid the loss of control over the workspace or build settings imposed by the use of these systems so I’d rather keep a workflow that can be used independent of these systems.

### Swift Package Manager

Which brings me to the [Swift Package Manager](https://github.com/apple/swift-package-manager); a combined build-system and dependency manager.

Does the Swift Package Manager offer anything new compared to the previous options I’ve mentioned? Well, it offers a new build system but my primary motivation here is dependency management; I wasn’t looking for a build system.

Using the Swift Package Manager isn’t going to have the weird effects on the repository that git submodules have. It is also bundled with Swift, so it’s a lower friction option than CocoaPods or Carthage – although I still don’t want to force users of my library to use the Swift Package Manager.

Is it possible to use the Swift Package Manager as a dependency resolver without using it as a build system?

## Hoping for the future

When I said “my primary motivation here is dependency management; I wasn’t looking for a build system”, I wasn’t being totally honest. I _should_ be primarily motivated by dependency management but truthfully, I’d also like to play around with the Swift Package Manager build system.

Like [Apache Maven](https://maven.apache.org) or [Rust Cargo](https://github.com/rust-lang/cargo), the Swift Package Manager includes a convention-based build system. While some metadata is declared in a top-level manifest, the build is, as much as possible, determined by the organization of files in the repository. I’m a big fan of this type of build system; a build shouldn’t require substantial configuring. Assuming folder structure conventions are followed, it should be possible to infer most – even all – parameters for a build, rather than forcing the programmer to manually enumerate all aspects, every time.

I would like to see Swift Package Manager projects become a project type in Xcode. Automatically keeping files sensibly in module folders rather than arbitrarily distributed around the filesystem and needing constant sheparding. Build settings inferred rather than configured through a vast array of tabs and inspectors. Dependencies viewable like the Xcode “Debug Memory Graph” display.

Obviously, though, Xcode doesn’t support the Swift Package Manager, yet (Swift Package Manager supports Xcode but it’s the other direction that’s more interesting to me). And, bluntly, until the Swift Package Manager can build apps, build for iOS, build for watchOS, build for tvOS, build mixed language modules, build bundles with resources, manage separate dependencies for tests or inline across modules, it won’t satisfy all the requirements of even a relatively simple library like CwlSignal.

But I’d still like to support the Swift Package Manager as a _secondary_ build option in the hope that it in a couple years it will be possible to make it the _primary_ option.

## Swift package fetch

Wanting to use the Swift Package Manager for dependency management but not as the primary build system creates some problems.

Summarizing what need to be done:

1. Support the Swift Package Manager (for both building and fetching dependencies)
2. Make Xcode projects refer to the files downloaded by Swift Package Manager.
3. Make everything transparent to the user.

### 1. Support the Swift Package Manager

Setting up the “Package.swift” file, adding semantic version tags to repositories and making sure that dependencies are fetched is trivial.

The signficant work was actually across the following tasks (in no particular order):

1. Reorganize my folders to follow the convention-based structure expected by the Swift Package Manager (all projects).
2. Separate my mixed Objective-C/Swift modules into separate modules (all projects except CwlSignal).
3. guard, be certain to

  the new modules created by the separation in step 2 (all projects except CwlSignal).
4. Separate my “.h” files so that they can be included from a project-wide umbrella header as in Xcode or from a module header as in Swift-PM (all projects except CwlSignal).
5. were

  so they remained accessible (CwlCatchException).
6. or other conditions not set by the Swift Package Manager (CwlDeferredWork and tests in CwlUtils and CwlSignal).
7. In Objective-C files that needed to both reference and be referenced by Swift, changed the references from Objective-C to Swift to dynamic lookups to avoid circular module dependencies (CwlMachBadInstructionHandler).
8. Move Info.plist files around. These are generated automatically by the Swift-PM but must manually exist for Xcode – Swift-PM must be set to ignore them all (all projects).

There was also a non-zero amount of effort involved in accepting how the conventions of the Swift Package Manager work and letting it guide some aspects of the build.

### 2. Make Xcode projects refer to the files downloaded by Swift Package Manager

In Swift 3.0, dependencies are placed in “./Packages/ModuleName-X.Y.Z” where X.Y.Z is the semantic version tag of checkout. Obviously, this will change if you ever change the version depended upon.

Swift 3.1 and later place dependencies in “./.build/checkout/ModuleName-XXXXXXXX” where XXXXXXXX is a hash derived from the repository URL. The hash is not guaranteed to be stable and as far as I can tell, the path format is undocumented and subject to change.

Clearly, we can’t point Xcode directly at either of these since they’re subject to change. We need to create symlinks from a stable location to these subject-to-change locations. This means that we need a simple way to determine the current locations.

The closest we get to a documented solution for handling these paths is the output to the following command:

```
swift package show-dependencies --format json
```

The output from this command offers a JSON structure that includes the module names and the checkout paths. While there’s no guarantee that this structure will remain stable in the future, it is _currently_ stable across 3.0 and 3.1 so it’s better than simply enumerating directories.

We need to create symlinks from a stable location to the locations detailed in this JSON file.

I chose to use the location “./.build/cwl_symlinks/ModuleName” to store a symlink to the actual location used by either Swift 3.0 or Swift 3.1 package managers. This creates the minor risk of collision in the scenario where two dependencies have the same module name but different origin or version but outside of that possibility it should offer a stable location that my Xcode projects can use to find these dependencies. When I change the version of a library that I depend upon or the hash changes (because I’m switching between local and remote versions of a repository for testing) or something else that affects the path, all we’ll need to do is update the symlink.

Getting Xcode to keep a path through the symlink rather than immediately resolve the symlink is a little tricky. While using Swift 3.1, I actually created a duplicate of each “./.build/checkout/ModuleName-XXXXXXXX” folder at the “./.build/cwl_symlinks/ModuleName” location, added all the files to Xcode before deleting the duplicate and creating a symlink at “./.build/cwl_symlinks/ModuleName” pointing to “./.build/checkout/ModuleName-XXXXXXXX”.

### 3. Making everything transparent to the user

We now have two non-transparent steps that we need to eliminate:

1. to get the dependencies.
2. Create symlinks in a stable location for all dynamically fetched dependencies.

For this, we’ll need some kind of automated script.

## Some kind of automated script

We need a “Run script” build phase at the top of any Xcode target with external dependencies. If you have multiple targets with external dependencies, it might be best to do this in its own “Aggregate” target (e.g. named “FetchDependencies”) and have other targets depend on the “Aggregate”.

When you add a “Run script” build phase to Xcode, it defaults to “/bin/sh”. I got about 5 lines into that before remembering that I’m terrible at bash so I change the “Shell” value for the build phase to `/usr/bin/xcrun --sdk macosx swift -target x86_64-apple-macosx10.14` (since I need to ensure the macOS SDK is used, even when building targets for iOS or other platforms) and set the script to the following code. Some of the parsing and configuring is a little dense but you should be able to read the comments to get a general feel for what’s happening.

```swift
import Foundation

func env(_ key: String) -> String? { return ProcessInfo.processInfo.environment[key] }
extension FileHandle: TextOutputStream {
    public func write(_ string: String) { string.data(using: .utf8).map { write($0) } }
    static var err = FileHandle.standardError
}
extension Process {
    struct Failure: Error {
        let code: Int32
        let output: String
    }
    convenience init(path: String, directory: URL? = nil, environment: [String: String]? = nil,
       arguments: String...) {
        self.init()
        (self.launchPath, self.arguments) = (path, arguments)
        _ = directory.map { self.currentDirectoryPath = $0.path }
        _ = environment.map { self.environment = $0 }
    }
    func printInvocation() -> Process {
        print("\(self.launchPath ?? "") \(self.arguments?.joined(separator: " ") ?? "")",
           to: &FileHandle.err)
        return self
    }
    @available(OSX 10.13, *) func runToString() throws -> String {
        let pipe = Pipe()
        self.standardOutput = pipe
        try self.run()
        let result = String(data: pipe.fileHandleForReading.readDataToEndOfFile(), encoding: .utf8) ?? ""
        self.waitUntilExit()
        if terminationStatus != 0 { throw Failure(code: terminationStatus, output: result) }
        return result
    }
}

@available(OSX 10.13, *)
struct PackageFetch {
    enum Failure: Swift.Error {
        case disablingInFavorOfCarthage
        case fetchAlreadyProcessed
        case missingEnvironment(String)
        case cantCreateOutputFile(String)
    }
    struct DependencyParseFailure: Error {
        let srcRoot: URL
        let description: Dictionary<String, Any>
        let topLevelPath: String
    }
    
    let toolchainDir: String
    let projectName: String
    let srcRoot: URL
    let packageDir: URL
    let symlinksURL: URL
    
    static func requireEnv(_ key: String) throws -> String {
        guard let value = env(key) else { throw Failure.missingEnvironment(key) }
        return value
    }
    
    init() throws {
        self.toolchainDir = try PackageFetch.requireEnv("TOOLCHAIN_DIR")
        self.srcRoot = URL(fileURLWithPath: try PackageFetch.requireEnv("SRCROOT"))
        self.projectName = try PackageFetch.requireEnv("PROJECT_NAME")
        self.packageDir = srcRoot.appendingPathComponent(".build")
        self.symlinksURL = packageDir.appendingPathComponent("symlinks")
    }
    
    func resolve() throws {
        print("### Starting package resolve into \(packageDir.path)", to: &FileHandle.err)
        
        let resolveOutput = try Process(
            path: toolchainDir + "/usr/bin/swift",
            directory: srcRoot,
            arguments: "package", "--build-path", "\(packageDir.path)", "resolve"
        ).printInvocation().runToString()
        
        if resolveOutput == "" {
            print("### All dependencies up-to-date.", to: &FileHandle.err)
        } else {
            print(resolveOutput, terminator: "")
        }
    }
    
    func showDependencies() throws -> String {
        print("### Runing swift package show-dependencies to get package locations", to: &FileHandle.err)
        return try Process(
            path: toolchainDir + "/usr/bin/swift",
            directory: srcRoot,
            arguments:
               "package", "--build-path", "\(packageDir.path)", "show-dependencies", "--format", "json"
        ).printInvocation().runToString()
    }
    
    static func createSymlink(link: URL, destination: URL) throws {
        let current = try? FileManager.default.destinationOfSymbolicLink(atPath: link.path)
        if current == nil || current != destination.relativePath {
            _ = try? FileManager.default.removeItem(at: link)
            try FileManager.default.createSymbolicLink(atPath: link.path,
               withDestinationPath: destination.relativePath)
            print("Created symbolic link: \(link.path) -> \(destination.relativePath)", to: &FileHandle.err)
        }
    }
    
    func createSymlink(srcRoot: URL, name: String, destination: String) throws {
        let linkLocation = symlinksURL.appendingPathComponent(name)
        let linkDestination = URL(fileURLWithPath: "../\(destination)", relativeTo: linkLocation)
        try PackageFetch.createSymlink(link: linkLocation, destination: linkDestination)
    }
    
    func traverse(srcRoot: URL, description: Dictionary<String, Any>, topLevelPath: String) throws {
        guard let dependencies = description["dependencies"] as? [Dictionary<String, Any>] else { return }
        for dependency in dependencies {
            guard
                let path = dependency["path"] as? String,
                let relativePath = (path.range(of: topLevelPath)?.upperBound).map({ String(path[$0...]) }),
                let name = dependency["name"] as? String
                else {
                    throw DependencyParseFailure(srcRoot: srcRoot, description: description,
                       topLevelPath: topLevelPath)
            }
            
            let dependencyBuildDir = URL(fileURLWithPath: path).appendingPathComponent(".build")
            try FileManager.default.createDirectory(at: dependencyBuildDir,
               withIntermediateDirectories: true, attributes: nil)
            try PackageFetch.createSymlink(
               link: dependencyBuildDir.appendingPathComponent("symlinks"), destination: symlinksURL)
            
            let dependencies = dependencyBuildDir.appendingPathComponent("dependencies-state.json")
            guard FileManager.default.createFile(atPath: dependencies.path, contents: nil) else {
                throw PackageFetch.Failure.cantCreateOutputFile(dependencies.path)
            }
            
            try createSymlink(srcRoot: srcRoot, name: name, destination: relativePath)
            try traverse(srcRoot: srcRoot, description: dependency, topLevelPath: topLevelPath)
        }
    }
    
    func parseAndCreateSymlinks(dependencies: String) throws {
        guard
            let jsonStartIndex = dependencies.index(of: "{"),
            let descriptionData = String(dependencies[jsonStartIndex...]).data(using: .utf8),
            let description = try JSONSerialization.jsonObject(with: descriptionData, options: [])
               as? Dictionary<String, Any>
            else {
                throw DependencyParseFailure(srcRoot: srcRoot, description: [:],
                   topLevelPath: packageDir.path + "/")
        }
        try FileManager.default.createDirectory(at: symlinksURL, withIntermediateDirectories: true,
           attributes: nil)
        try traverse(srcRoot: srcRoot, description: description, topLevelPath: packageDir.path + "/")
    }
    
    static func fetch() throws {
        guard env("CARTHAGE") != "YES" else { throw Failure.disablingInFavorOfCarthage }
        guard env("CWL_PACKAGE_DIR") == nil else { throw Failure.fetchAlreadyProcessed }
        
        let fetch = try PackageFetch()
        try fetch.resolve()
        let dependencies = try fetch.showDependencies()
        try fetch.parseAndCreateSymlinks(dependencies: dependencies)
        print("### Complete.", to: &FileHandle.err)
    }
}

if #available(OSX 10.13, *) {
    do {
        try PackageFetch.fetch()
    } catch PackageFetch.Failure.disablingInFavorOfCarthage {
        print("Fetching using swift package manager disabled in favor of Carthage", to: &FileHandle.err)
    } catch PackageFetch.Failure.fetchAlreadyProcessed {
        print("Package fetching disabled in child build", to: &FileHandle.err)
    } catch {
        print("Failed: \(error)", to: &FileHandle.err)
        exit(1)
    }
} else {
    print("Failed: script must run on mac OS X 10.13 or newer", to: &FileHandle.err)
    exit(1)
}
```

Compiling and running this code takes about a second but it would still be better to avoid that overhead after the first run. You can add `$(SRCROOT)/Package.swift` to the “Input Files” list for the Run Script and add one of `$(SRCROOT)/.build/cwl_symlinks/ModuleName` (where “ModuleName” is a modules fetched by the task) for each dependency fetched by the Swift Package Manager. This will prevent Xcode re-running unless the “Package.swift” file changes or the module symlink is deleted, eliminating that additional second of overhead.

> **Irony note:** To avoid the static inclusion of dependencies, I’ve statically included this file in each repository.

## Try it out

~~You can inspect or download the [CwlCatchException](https://github.com/mattgallagher/CwlCatchException), [CwlPreconditionTesting](https://github.com/mattgallagher/CwlPreconditionTesting), [CwlUtils](https://github.com/mattgallagher/CwlUtils) and [CwlSignal](https://github.com/mattgallagher/CwlSignal) projects from github. All dependencies are now fetched using “swift package fetch”.~~

### Update 2018

Due to friction with Xcode 10’s “new build system”, I’ve ceased using this approach in my own code.

While I was able to migrate this approach to Xcode 10 – [see the Sep 30 commit for CwlSignal](https://github.com/mattgallagher/CwlSignal/tree/3d6c6d11171f93dd52d6b827da2775c9c79ba64d) – the effort involved, the fragility and the compromises required made me abandon the whole approach. I’ve reverted to using submodules.

Technically, the package fetching with the above script continues to work well. The problem ends up being the difficulty of building projects fetched in this way within Xcode. Thinking the projects are gone, Xcode discards references to files in child projects. The new build system refuses to start when it can’t find all required inputs. And on top of everything, I was not able to get Xcode’s indexer to find the underlying source code for dependencies – jumping only to the generated interfaces which is a poor experience when you have the full source code.

Read more about the difficulty around Xcode’s “new build system” in [Article updates, 2018 edition](https://www.cocoawithlove.com/blog/updating-for-2018.html).

## Conclusion

If it was possible to completely switch to the Swift Package Manager for all use cases, then that would be the end of the story and everything would be a lot cleaner. Unfortunately, current versions of the Swift Package Manager can’t handle a large number of build scenarios (including apps and iOS/watchOS/tvOS platforms) so it’s necessary to keep Xcode as the primary build environment and that means integrating the two.

The “Run Script” build phase works pretty well to hide fetch machinery. Things are going to fail if you don’t have a internet connection when trying to build for the first time, but otherwise it should be transparent and effortless. By setting the “Input Files and “Output Files” for the “Run Script” build step, the minor overhead of compiling and running this step is eliminated in almost all cases so it’s very low interference.

Unfortunately, it wasn’t really worth the effort to keep this approach working in the long run and I’ve reverted to using git subtrees. I don’t know why Apple keep dragging their feet on bringing package management support to Xcode but it can’t come soon enough.
