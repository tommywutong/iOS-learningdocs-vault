---
title: Developing for the App Store
apple_id: TP40011186
resource_type: Guide
platform: iOS|macOS
topic: General
technology: null
published: '2013-04-23'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/ApplicationDevelopmentOverview/CreateYourDevelopmentTeam/CreateYourDevelopmentTeam.html
archived_at: '2026-07-15T07:33:28.731820Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Developing for the App Store](About%20the%20Application%20Development%20Process.md)


[Next](Creating%20a%20Project.md)[Previous](Building%20an%20App%20for%20the%20App%20Store.md)

# Preparing the Development Team

Most people think of a development team as a group of programmers, designers, and artists who work together to develop an app. That explanation is also true when you develop for iOS or OS X, but it isn’t complete. A development team takes on the additional meaning of a group created and managed on the Apple Developer website. Some additional tasks during the development process are performed using this development team you’ve created. If you create a team with yourself as the only member, you take on all of these tasks. If you are part of a larger team, the work and the responsibilities may be divided between the group.

Each person on the development team has a unique _Apple ID_, an account used by the developer programs to authenticate that person. Further, access privileges can be configured separately for each person. This flexibility allows your team to restrict critical tasks, such as publishing the app on the App Store, to a small subset of its participants.

This chapter starts by describing the various roles that members of a team may fill. It then provides guidance about how you may want to go about organizing the team. Finally, it describes work the team must do to allow people of the team to sign apps. Figure 2-1 shows all of the required steps.

__Figure 2-1__  Steps to create a development team

!

To start, one person must enroll in either the iOS or OS X developer program; this person becomes the _team agent_ for the team. The team agent may enroll in both programs if your team intends to develop apps for both operating systems. During this step, the team agent signs the legal agreements required to become an Apple developer and prepares the financial paperwork so that the team can be paid for purchases from the App Store.

The team agent is special; he or she has unrestricted access to the team and is legally responsible for the team. The team agent also performs most of the tasks to organize the team. If desired, after others have joined the team, the team agent can delegate some of this authority to other members of the team, allowing those others to perform these tasks instead.

The team agent might need to sign updated or new licensing agreements, particularly when the team wants to incorporate specific technologies into an app. For example, an app that uses the iAd service requires your team agent to sign a separate agreement.

After the team agent has joined a developer program, he or she adds other people to the team and sets their privileges. If you are the team agent and the sole developer on your team, no additional configuration is needed, because the team agent always has access to all account features. However, you should continue to read this section to understand the kinds of tasks you may need to perform throughout the rest of the development process.

To add a new person to the team, the team agent sends an invitation to the person; part of sending an invitation includes setting that person’s privileges on the team. When he or she accepts the invitation, that person is automatically added to the team.

A person’s membership level on the team defines the level of access he or she has to the Apple developer webpages and the team information stored there. This privilege level extends to the kinds of tasks that developer is allowed to perform on behalf of the team. For example, only certain members of the team are allowed to publish apps on the App Store. By giving you control over these task privileges, Apple makes it easier for you to maintain good security practices for the team.

If the team has joined multiple developer programs, when you configure a person’s privileges, you set a separate privilege level for each program. You can also choose to not give someone access to a program.

Table 2-1 lists the roles a team participant can play and provides a basic description of each. Each level of access includes all the capabilities of the levels below it.

__Table 2-1__  Team roles

| Role | Description |
| Team agent | A _team agent_ is legally responsible for the team and acts as the primary contact with Apple. The team agent can change the access level of any other member of the team. |
| Team admin | A _team admin_ can set the privilege levels of other participants, although a team admin cannot demote the team agent. Team admins manage all assets used to sign your apps, either during development or when your team is ready to distribute an app. Team admins are the only people on a team that can sign apps for distribution on nondevelopment devices. Team admins also approve signing certificate requests made by team members. |
| Team member | A _team member_ gains access to prerelease content delivered by Apple on that program’s portal. A team member can also sign apps during development, and but only after he or she makes a request for a development signing certificate and has that request approved by a team admin. |

Table 2-2 drills deeper into this list of privileges granted to members of your team. Although this document hasn’t explained all these privileges, most will be clear to you by the time you finish reading it.

__Table 2-2__  Privileges assigned to each membership level

| Privilege | Team agent | Team admin | Team member |
| Legal responsibility for the team | ../Art/checkmark.png | ../Art/x.png | ../Art/x.png |
| Primary contact with Apple | ../Art/checkmark.png | ../Art/x.png | ../Art/x.png |
| Invite team admins and team members | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Approve a request for a development signing certificate | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Add devices for development and user testing | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Create app IDs | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Request a distribution signing certificate from Apple | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Create development and distribution provisioning profiles | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Enable app IDs to use Apple Push Notification or In-App Purchase | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Create SSL certificates for the Apple Push Notification Service | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Request a development signing certificate | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/checkmark.png |
| Download development provisioning profiles | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/checkmark.png |
| View prerelease website content | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/checkmark.png |

The privileges set in the previous section primarily pertain to the development process: They define who is allowed to sign apps, who is allowed to create signing certificates, and so on. However, the team agent also manages access privileges to the iTunes Connect website. For example, changing the price of an app is a task you likely want to limit to a small number of people on your team. Access to the iTunes Connect website is configured separately and is designed to be more fine-grained than the access you set in Member Center. On iTunes Connect, each person on the team can be assigned one or more roles; each role has different privileges. Table 2-3 describes the roles at a high level.

__Table 2-3__  iTunes Connect roles and responsibilities

| Role | Responsibilities |
| Legal | The legal role is automatically assigned to the team agent, and only the team agent is permitted to have this access. The legal role allows the team agent to sign legal contracts and other agreements. |
| Admin | The admin role grants access to all tasks in iTunes Connect except for those assigned to the legal role. A team agent is always assigned the admin role, and this access cannot be revoked without changing which person on the team acts as the team agent. An admin can assign iTunes Connect roles to other people on the team. |
| Finance | The finance role grants access to financial reports and sales information. The finance role also authorizes the person to view contract, tax, and banking information. |
| Sales | The sales role grants access only to sales data. |
| Technical | The technical role grants the ability to edit the app information stored in iTunes Connect and to create test accounts needed to test In-App Purchase support in an app. |

Table 2-4 lists the most common modules you need to access in iTunes Connect, along with the roles that are allowed to access each module. The legal role is not shown, because only the team agent has those rights. All participants have the ability to edit their own personal details stored in their accounts in iTunes Connect.

__Table 2-4__  Abbreviated list of iTunes Connect modules, including availability by role

| Responsibility | Admin | Finance | Sales | Technical |
| Manage Users | ../Art/checkmark.png | ../Art/x.png | ../Art/x.png | ../Art/x.png |
| Manage Your Applications | ../Art/checkmark.png | ../Art/x.png | ../Art/x.png | ../Art/checkmark.png |
| Manage Test Users | ../Art/checkmark.png | ../Art/x.png | ../Art/x.png | ../Art/checkmark.png |
| Sales and Trends | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png |
| Contracts, Tax, and Banking | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png | ../Art/x.png |
| Payments and Financial Reports | ../Art/checkmark.png | ../Art/checkmark.png | ../Art/x.png | ../Art/x.png |

Now that you understand the roles people can assume in Member Center and iTunes Connect, you should consider how you want to organize the team. Organizing the team requires more than setting privileges described above. The size of the team affects how you organize it and its assets.

The smallest team is a single person—you. You act as the team agent and have full privileges to perform any task. The disadvantage of a one-person team is that you have to do all the work. You need to set up the assets needed to sign and publish an app, configure all the information in iTunes Connect, develop an app, and market it.

__Figure 2-2__  An individual is the team agent

!

A more common configuration is a small developer team. On a small team, the team agent is also a programmer, but defers some of the administration overhead to another person on the team. The team agent handles all of the financial and sales operations for the team, while the team admin ensures that the developers on the team have what they need to get the job done.

__Figure 2-3__  A small development team

!

If your team is large, you can divide the tasks further. Some people on the team might not be programmers, including the team admin. The sales and financial roles might be filled by people with a business background. You might even have in-house testers who are not also programmers. The task of creating and shipping apps could be delegated to one or more dedicated team admins. You might even partition the work further and divide the team between iOS and OS X development.

__Figure 2-4__  A large development team

!

As the team grows, the need for coordination between the different people on the team increases. In particular, the cost of development errors increases when you have more programmers on the team. For example, if you are the sole member of the team, you can store all your work on a single computer and do all of the work there. Xcode even allows you to create a local source code repository to store your code. But what happens when the team grows in size?

When the team grows to a moderate size, you need more infrastructure. You want a separate computer to act as a remote source code repository; members of the team pull down the code from the remote repository to their computers, make changes, and send those changes back to the server. But when multiple developers are syncing code, the chance of an error being checked into the code increases. To minimize problems, you usually want multiple branches of development, including stable branches that hold the code you use to build your shipping app and experimental or developmental branches used for new development. These strategies require a deeper understanding of the underlying source code repository and require you to define specific policies that describe how code gets integrated between the different branches you maintain.

If your team grows very large, checking erroneous code into developmental branches could impair your team’s productivity. By the time you discover an error, it might already have been synced to other people’s computers. After you correct the error, propagating the fixes to everyone on the team still takes time. The frequency of such incidents and the time lost for each incident increase as the size of the team increases; these losses, when aggregated, cripple your team’s effectiveness. To avoid this lost productivity, you should add additional infrastructure for code management. For example, you might adopt a process of continuous integration by creating a dedicated build machine (known as a build bot) that automatically checks out each change and rebuilds your app. By building new changes as they arrive, you discover errors earlier; you might even configure the server to back out such changes before others on the team pull down the offending code. If your project includes unit tests or automated user tests, the build computer can also run those tests to verify that your source code still passes the tests. This process, known as _smoke testing_, increases the team’s confidence that code stored in the development branches builds and works properly.

As the team grows larger, you want to automate tasks that are repeatable, predictable, and costly to perform by hand. By automating common tasks, you reduce the burden on the team and allow it to focus on designing and implementing code.

Apps distributed on the App Store must be cryptographically signed. You may also need to sign the app during development.

- On OS X, an app must be signed during development if it uses iCloud or application sandboxing.
- On iOS, all apps must be signed during development.

Regardless of which platform you are developing for, everyone on the team should understand the code signing process. This section describes the assets that are needed to sign an app and authorize it to run on a device, and then explains how people on the team acquire the assets they need to sign apps. Some of these assets should be created now as you organize your team; the rest are created each time you start a new project.

Figure 2-5 shows everything that is needed to build and sign an iOS app during development. Signing apps during OS X development or signing to distribute an app on either platform follows similar procedures. For now, focus on this example. While you are developing an iOS app, it can only be installed on iOS devices specifically marked for development. To run an app on such a development device, you install a signed version of the app and a _development provisioning profile_ that authorizes the signed app to be launched. Without a profile that authorizes it to launch, iOS prevents the app from launching.

__Figure 2-5__  Overview of the iOS development provisioning process

!

Creating development provisioning profiles is described in detail in [Creating a Project](Creating%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobwfvbuqnrnknltg); for now, understand that a development provisioning profile is a signed file whose contents define the scope of the profile:

- The development profile authorizes a specific set of apps to run.
- The development profile authorizes a specific list of devices to run those apps.
- The development profile authorizes a specific list of development certificates to sign those apps.

In addition to being installed on the development device, the profile must be installed on your development computer also. The profile authorizes the copy of Xcode to sign the app. Xcode only signs an app and installs it on the device if the profile authorizes the signing certificate and the app being signed. Logically, this makes sense; if a profile that authorizes the app to launch is not available, such an signed app would serve no purpose.

Next, take a close look at the left side of Figure 2-5. To sign code during development, you need the following items installed in the keychain on your development system:

- A private key.
- A _development signing certificate_ (authorized by a team admin). This signing certificate includes the public key associated with the private key.
- An intermediate signing certificate (provided by Apple). This certificate acts as an intermediary between your development signing certificate and the signing authority.

The combination of a signing certificate and the corresponding private key is called a _code signing identity_. When you build an iOS app, Xcode compiles it, signs it using your code signing identify, and installs it on the device. If a provisioning profile compatible with the signed app is also installed on the device, you can launch and debug the app.

Figure 2-6 shows the process for setting up a new developer on the team. The full details of this process are spelled out in documents listed later in this chapter; see [To Learn More](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcobwfvbuqnjnknltcoa). For now, you only need to understand this process at a high level. Team members make requests; team admins authorize or deny these requests. There are two separate pieces that need to be authorized: adding a development device to the team’s devices and creating the code signing identity used to sign apps during development.

__Figure 2-6__  The process for approving a device and getting a signing certificate

!

To add a device to the team, you send the _unique device ID (UDID)_ for the device to a team admin; this process happens outside of any tools provided by Apple. For example, you might send an email to the team admin with the device’s device ID. The team admin adds the device to the team’s devices. Typically, the team admin also adds this device to any development provisioning profiles associated with the team, although that is not strictly required. For example, if your team wants to limit an app to specific devices, then you might choose to add the device only to a subset of the team’s profiles.

To get a signing certificate, a team member uses Xcode to request a signing certificate. Xcode automatically creates a new public and private key and requests that a new development signing certificate be created for the team member. After a team admin receives and approves the certificate request, the team member can use Xcode to automatically install the required pieces into the keychain.

Although setup is described here as a single process, you do not need to perform both steps for every member of your team. For example, you might want internal testers to be associated with the development team on the Apple Developer website but not allow those testers to build and sign your app. In this case, the team admin might include a tester’s device in the team’s devices but not allow the tester to create a code signing identity. Similarly, an external tester’s device must be included in the team’s device list in order for it to be authorized to run an app.

While the above discussion was about development signing certificates, when you organize your team, the team should also request a _distribution signing certificate_. A distribution signing certificate is required if you intend to distribute apps to nondevelopment devices. Unlike development signing certificates, where each team member has a separate code signing identity, a team has a only one code signing identity used to sign apps for distribution. The procedure for creating a distribution certificate is similar to the workflow described above, but the request for a distribution signing certificate is made by a team admin using a new public/private key pair and Apple approves the request. After the certificate is approved by Apple, only a team admin can download the resulting certificate.

If you are on an iOS team, read the following documents to learn more about creating a team and setting up its signing certificates:

- If you are a team admin, read _[iOS Team Administration Guide](../../Tools%20Languages/iOS%20Team%20Administration%20Guide/About%20iOS%20Development%20Team%20Administration.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnjz)_.
- If you are a team member, read _Tools Workflow Guide for iOS_.
- Read [iTunes Connect Development Guide](https://itunesconnect.apple.com/docs/iTunesConnect_DeveloperGuide.pdf) for a comprehensive description of iTunes Connect and the tasks you perform there.

If you are on an OS X team, read the following documents to learn more about creating a team and setting up its signing certificates:

- Regardless of whether you are a team member or a team admin, read _Tools Workflow Guide for Mac_.
- Read [iTunes Connect Development Guide](https://itunesconnect.apple.com/docs/iTunesConnect_DeveloperGuide.pdf) for a comprehensive look at iTunes Connect and the tasks you perform there.

[Next](Creating%20a%20Project.md)[Previous](Building%20an%20App%20for%20the%20App%20Store.md)

