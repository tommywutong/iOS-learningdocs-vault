---
title: How AI Is Transforming the Adoption of Secure-by-Default Mobile Frameworks
source: Meta Engineering — iOS
source_key: fbeng
source_url: 'https://engineering.fb.com/2025/12/15/android/how-ai-transforming-secure-by-default-mobile-frameworks-adoption/'
original_language: en
published: 2025-12-15
status: active
license: © Meta → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:693e9090b35859bb'
translated: false
---

> 原文：[How AI Is Transforming the Adoption of Secure-by-Default Mobile Frameworks](https://engineering.fb.com/2025/12/15/android/how-ai-transforming-secure-by-default-mobile-frameworks-adoption/)　·　Meta Engineering — iOS

- Meta’s secure-by-default frameworks wrap potentially unsafe OS and third-party functions, making security the default while preserving developer speed and usability.
- These frameworks are designed to closely mirror existing APIs, rely on public and stable interfaces, and maximize developer adoption by minimizing friction and complexity.
- Generative AI and automation accelerate the adoption of secure frameworks at scale, enabling consistent security enforcement and efficient migration across Meta’s vast codebase.

Sometimes functions within operating systems or provided by third parties come with a risk of misuse that could compromise security. To mitigate this, we wrap or replace these functions using our own secure-by-default frameworks. These frameworks play an important role in helping our security and software engineers maintain and improve the security of our codebases while maintaining developer speed.

But implementing these frameworks comes with practical challenges, like design tradeoffs. Building a secure framework on top of Android APIs, for example, requires a thoughtful balance between security, usability, and maintainability.

With the emergence of AI-driven tools and automation we can scale the adoption of these frameworks across Meta’s large codebase. AI can assist in identifying insecure usage patterns, suggesting or automatically applying secure framework replacements and continuously monitoring compliance. This not only accelerates migration but also ensures consistent security enforcement at scale.

Together, these strategies empower our development teams to ship well-secured software efficiently, safeguarding user data and trust while maintaining high developer productivity across Meta’s vast ecosystem.

## How We Design Secure-by-Default Frameworks at Meta

Designing secure-by-default frameworks for use by a large number of developers shipping vastly different features across multiple apps is an interesting challenge. There are a lot of competing concerns such as discoverability, usability, maintainability, performance, and security benefits.

Practically speaking, developers only have a finite amount of time to code each day. The goal of our frameworks is to improve product security while being largely invisible and friction-free to avoid slowing developers down unnecessarily. This means that we have to correctly balance all those competing concerns discussed above. If we strike the wrong balance, some developers could avoid using our frameworks, which could reduce our ability to prevent security vulnerabilities.

For example, if we design a framework that improves product security in one area but introduces three new concepts and requires developers to provide five additional pieces of information per call site, some app developers may try to find a way around using them. Conversely, if we provide these same frameworks that are trivially easy to use, but they consume noticeable amounts of CPU and RAM, some app developers may, again, seek ways around using them, albeit for different reasons.

These examples might seem a bit obvious, but they are taken from real experiences over the last 10+ years developing ~15 secure-by-default frameworks targeting Android and iOS. Over that time, we’ve established some best practices for designing and implementing these new frameworks.

To the maximum extent possible, an effective framework should embody the following principles:

- **The secure framework API should resemble the existing API.** This reduces the cognitive burden on framework users, forces security framework developers to minimize the complexity of the changes, and makes it easier to perform automated code conversion from the insecure to secure API usage.
- **The framework should itself be built on public and stable APIs**. APIs from OS vendors and third parties change all the time, especially the non-public ones. Even if access to those APIs is technically allowed in some cases, building on top of private APIs is a recipe for constant fire drills (best case) and dead-end investment in frameworks that simply can’t work with newer versions of operating systems and libraries (worst case).
- **The framework should cover the maximum number of application users, not security use cases**. There shouldn’t be one security framework that covers all security issues, and not every security issue is general enough to deserve its own framework. However, each security framework should be usable across all apps and OS versions for a particular platform. Small libraries are faster to build and deploy, and easier to maintain and explain to app developers.

Now that we’ve looked at the design philosophy behind our frameworks, let’s look at one of our most widely used Android security frameworks, SecureLinkLauncher.

## SecureLinkLauncher: Preventing Android Intent Hijacking

SecureLinkLauncher (SLL) is one of our widely-used secure frameworks. SLL is designed to prevent sensitive data from spilling through the[Android intents system](https://developer.android.com/guide/components/intents-filters). It exemplifies our approach to secure-by-default frameworks by wrapping native Android intent launching methods with scope verification and security checks, preventing common vulnerabilities such as intent hijacking without sacrificing developer velocity or familiarity.

The system consists of intent senders and intent receivers. SLL is targeted to intent senders.

SLL offers a semantic API that closely mirrors the familiar Android Context API for launching intents, including methods like startActivity() and startActivityForResult(). Instead of invoking the potentially insecure Android API directly, such as context.startActivity(intent);, developers use SecureLinkLauncher with a similar method call pattern, for example, SecureLinkLauncher.launchInternalActivity(intent, context);. Internally, SecureLinkLauncher delegates to the stable Android startActivity() API, ensuring that all intent launches are securely verified and protected by the framework.

```java
public void launchInternalActivity(Intent intent, Context context) {
   // Verify that the target activity is internal (same package)
   if (!isInternalActivity(intent, context)) {
       throw new SecurityException("Target activity is not internal");
   }
   // Delegate to Android's startActivity to launch the intent
   context.startActivity(intent);
}
```

Similarly, instead of calling context.startActivityForResult(intent, code); directly, developers use SecureLinkLauncher.launchInternalActivityForResult(intent, code, context);. SecureLinkLauncher (SLL) wraps Android’s startActivity() and related methods, enforcing scope verification before delegating to the native Android API. This approach provides security by default while preserving the familiar Android intent launching semantics.

One of the most common ways that data is spilled through intents is due to incorrect targeting of the intent. As an example, following intent isn’t targeting a specific package. This means it can be received by any app with a matching \<intent-filter\>. While the intention of the developer might be that their Intent ends up in the Facebook app based on the URL, the reality is that any app, including a malicious application, could add an \<intent-filter\> that handles that URL and receive the intent.

```java
Intent intent = new Intent(FBLinks.PREFIX + "profile");
intent.setExtra(SECRET_INFO, user_id);
startActivity(intent); 
// startActivity can’t ensure who the receiver of the intent would be
```

In the example below, SLL ensures that the intent is directed to one of the family apps, as specified by the developer’s scope for implicit intents. Without SLL, these intents can resolve to both family and non-family apps,potentially exposing SECRET_INFO to third-party or malicious apps on the user’s device. By enforcing this scope, SLL can prevent such information leaks.

```java
SecureLinkLauncher.launchFamilyActivity(intent, context); 
// launchFamilyActivity would make sure intent goes to the meta family apps
```

In a typical Android environment, two scopes – internal and external – might seem sufficient for handling intents within the same app and between different apps. However, Meta’s ecosystem is unique, comprising multiple apps such as Facebook, Instagram, Messenger, WhatsApp, and their variants (e.g., WhatsApp Business). The complexity of inter-process communication between these apps demands more nuanced control over intent scoping. To address this need, SLL provides a more fine-grained approach to intent scoping, offering scopes that cater to specific use cases:

- **Family scope**: Enables secure communication between Meta-owned apps, ensuring that intents are only sent from one Meta app to another.
- **Same-key scope**: Restricts intent sending to Meta apps signed with the same key (not all Meta apps are signed by the same key), providing an additional layer of security and trust.
- **Internal scope**: Restricts intent sending within the app itself.
- **Third-party scope**: Allows intents to be sent to third-party apps, while preventing them from being handled by Meta’s own apps.

By leveraging these scopes, developers can ensure that sensitive data is shared securely and intentionally within the Meta ecosystem, while also protecting against unintended or malicious access. SLL’s fine-grained intent scoping capabilities, which are built upon the secure-by-default framework principles discussed above, empower developers to build more robust and secure applications that meet the unique demands of Meta’s complex ecosystem.

## Leveraging Generative AI To Deploy Secure-by-Default Frameworks at Scale

Adopting these frameworks in a large codebase is non-trivial. The main complexity is choosing the correct scope, as that choice relies on information that is not readily available at existing call sites. While one could imagine a deterministic analysis attempting to infer the scope based on dataflows, that would be a large undertaking. Furthermore, it would likely have some precision-scalability trade-off.

Instead, we explored using Generative AI for this case. AI can read the surrounding code and attempt to infer the scope based on variable names and comments surrounding the call site. While this approach isn’t always perfect, it doesn’t need to be. It just needs to provide good enough guesses, such that code owners can one-click accept suggested patches.

If the patches are correct in most cases, this is a big timesaver that enables efficient adoption of the framework. This complements our [recent work on AutoPatchBench](https://engineering.fb.com/2025/04/29/ai-research/autopatchbench-benchmark-ai-powered-security-fixes/), a benchmark designed to evaluate AI-powered patch generators that leverage large language models (LLMs) to automatically recommend and apply security patches. Secure-by-default frameworks are a great example of the kinds of code modifications that an automatic patching system can apply to improve the security of a code base.

We’ve built a framework leveraging Llama as the core technology, which takes locations in the codebase that we want to migrate and suggests patches for code owners to accept:

![](https://engineering.fb.com/wp-content/uploads/2025/12/Meta-Secure-By-Default-frameworks.png)

### Prompt Creation

The AI workflow starts with a call site we want to migrate including its file path and line number. The location is used to extract a code snippet from the code base. This means opening the file where the call site is present, copying 10-20 lines before and after the call site location, and pasting this into the prompt template that gives general instructions as to how to perform the migration. This description is very similar to what would be written as an onboarding guide to the framework for human engineers.

### Generative AI

The prompt is then provided to a Llama model (llama4-maverick-17b-128e-instruct). The model is asked to output two things: the modified code snippet, where the call site has been migrated; and, optionally, some actions (like adding an import to the top of a file). The main purpose of actions is to work around the limitations of this approach where all code changes are not local and limited to the code snippet. Actions enable the model fix to reach outside the snippet for some limited, deterministic changes. This is useful for adding imports or dependencies, which are rarely local to the code snippet, but are necessary for the code to compile. The code snippet is then inserted back to the code base and any actions are applied.

### Validation

Finally, we perform a series of validations on the code base. We run all of these with and without the AI changes and only report the difference:

- Lints: We run the linters again to confirm the lint issue was fixed and no new lint errors were introduced by the changes.
- Compiling: We compile and run tests covering the targeted file. This is not intended to catch all bugs (we rely on continuous integration for that), but give the AI some early feedback on its changes (such as compile errors).
- Formatting: The code is formatted to avoid formatting issues. We do not feed the formatting errors back to the AI.

If any errors arise during the validation, their error messages are included in the prompt (along with the “fixed” code snippet) and the AI is asked to try again. We repeat this loop five times and give up if no successful fix is created. If the validation succeeds, we submit a patch for human review.

## Thoughtful Framework Design Meets Intelligent Automation

By adhering to core design principles such as providing an API that closely resembles existing OS patterns, relying solely on public and stable OS APIs, and designing frameworks that cover broad user bases rather than niche use cases, developers can create robust, secure-by-default features that integrate seamlessly into existing codebases.  
   
 These same design principles help us leverage AI for smoothly adopting frameworks at scale. While there are still challenges around the accuracy of generated code – for example, the AI choosing the incorrect scope, using incorrect syntax, etc., the internal feedback loop design allows the LLM to automatically move past easily solvable problems without human intervention, increasing scalability and reducing developer frustration.

Internally, this project helped prove that AI could be impactful for adopting security frameworks across a diverse codebase in a way that is minimally disruptive to our developers. There are now a variety of projects tackling similar problems across a variety of codebases and languages – including C/++ – using diverse models and validation techniques. We expect this trend to continue and accelerate in 2026 as developers become more comfortable with state of the art AI tools and the quality of code that they are capable of producing.

As our codebase grows and security threats become more sophisticated, the combination of thoughtful framework design and intelligent automation will be essential to protecting user data and maintaining trust at scale.
