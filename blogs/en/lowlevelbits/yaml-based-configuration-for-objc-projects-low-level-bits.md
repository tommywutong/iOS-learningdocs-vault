---
title: YAML-based Configuration for ObjC Projects - Low Level Bits 🇺🇦
source: Low Level Bits (Alex Denisov)
source_key: lowlevelbits
source_url: 'https://lowlevelbits.org/yaml-based-configuration-for-objc-projects/'
original_language: en
published: ''
status: active
license: © 2014-2025 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:2ad8fce4a5743154'
translated: false
---

> 原文：[YAML-based Configuration for ObjC Projects - Low Level Bits 🇺🇦](https://lowlevelbits.org/yaml-based-configuration-for-objc-projects/)　·　Low Level Bits (Alex Denisov)

# YAML-based Configuration for ObjC Projects

_Published on Feb 06, 2015_

Probably every iOS or OS X app has to deal with configurations such as server address, analytics service API key and so on. Usually these configurations are different for development and production environment, e.g.: “[https://staging.example.com](https://staging.example.com)” and “[https://example.com](https://example.com)”. Our toolchain does not provide good solution for this problem, so we have to implement our own.

When I worked with Ruby On Rails I really loved its approach for database configuration:

```yaml
development:
  user: dev
  password: dev123
# ...
production:
  user: root
  password: supersecurepassword
# ...
```

I wish I can use the same approach in my daily iOS development.

Fortunately, I can!

**TL;DR;**

Checkout project [xcconf](https://github.com/AlexDenisov/xcconf) and `Sample/Sample.xcodeproj`

### Commonly used mechanisms

There are at least two common approaches to separate configurations: preprocessor definitions and plist file. Both of them have serious disadvantages.

#### Preprocessor Definition

You may saw and probably used this approach. It’s pretty easy and simple to use:

```objectivec
#ifdef DEBUG
NSString *const kServerAddress = @"https://staging.example.com";
#else
NSString *const kServerAddress = @"https://example.com";
#endif
```

But let’s say that you add one more environment, e.g. “Beta” for beta testers. It means that you have to add new preprocessor definition and update all your constant declarations. Also, this approach is error prone: it’s really easy to make a typo or “accidentally” drop a definition. Your code will compile, but it’d use wrong environment. Though, this approach has at least one advantage: your code contains only things that you use, all the private data (addresses, keys) is not exposed.

#### Plist file

This is other commonly used mechanism. This approach described [here](http://code.tutsplus.com/tutorials/ios-quick-tip-managing-configurations-with-ease--mobile-18324). It’s also has some disadvantages: if you want to add new configuration variable - you have to add it to every subsection, also you need to add a property to class and write (copy-paste?) initialization code. Moreover, you will distribute all your keys/endpoints to the end user, or you’ll have to cleanup the file right before deploy to the AppStore. Still you have to perform way too many actions for such a simple task.

Thanks god there is more easier and robust way.

### XCCONF and YAML

[xcconf](https://github.com/AlexDenisov/xcconf) incorporates only best parts from methods described previously:

- all settings store in one place
- you don’t expose private data
- everything done at compile time

##### Here is how it looks like:

Configuration file:

```yaml
principalClass: Configuration

Debug:
  serverAddress: https://staging.example.com
  APIKey: qwe123!!qwe

Release:
  serverAddress: https://example.com
  APIKey: qwe123qwe
```

ObjC code:

```objectivec
@Interface Configuration : NSObject
- (NSString *)serverAddress;
- (NSString *)APIKey;
@end

// ...

Config *config = [Config new];
NSLog(@"%@", config.serverAddress);
```

No preprocessor, no boilerplate!

#### Installation and usage

To install `xcconf` you need to clone repo and run one command, it’ll build executable and install it into `/usr/local/bin`

```bash
git clone [email protected]:AlexDenisov/xcconf.git && cd xcconf
make install
```

Integration into project looks weird, but don’t worry, that’s ok :)

First of all create YAML file, e.g,: `config.yaml`

![New file](https://lowlevelbits.org/img/yaml-based-configuration/new_file.png)

Put there initial configuration:

```yaml
principalClass: Config

Debug:
  color: Green

Release:
  color: Blue
```

Prepare class interface for configuration. **But do not create implementation**. Its name should be equal to `principalClass` and it might contain getter methods for all available parameters, in this case it’s just `color`

```objectivec
@interface Config : NSObject
- (NSString *)color;
@end
```

Let’s now compile our config, go to `Build Phases` -\> `Compile Sources` -\> `+` and add `config.yaml`

![Compile YAML](https://lowlevelbits.org/img/yaml-based-configuration/compile_yaml.png)

Obviously Xcode doesn’t have YAML compiler, but we can provide our own. Open `Build Rules`, add new one that matches files with pattern `*.yaml` and run shell command `/usr/local/bin/xcconf`. Also, we need to specify output file, otherwise it won’t work: `$(DERIVED_FILE_DIR)/xcconf.m`. Make sure that output file has extension `.m`, so that Xcode can compile it and provide implementation for the `principalClass`.

![xcconf](https://lowlevelbits.org/img/yaml-based-configuration/xcconf.png)

Now we’re ready to use it:

```objectivec
#import "Config.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        Config *config = [Config new];
        NSLog(@"%@", config.color);
    }
    return 0;
}
```

Build&Run:

![output](https://lowlevelbits.org/img/yaml-based-configuration/output.png)

### Summary

The project is very young, I did start one day ago, so it can have (it definitely has) some problems and might be improved.

I’d really appreciate any feedback.

P.S. Pull Requests are welcome! :)
