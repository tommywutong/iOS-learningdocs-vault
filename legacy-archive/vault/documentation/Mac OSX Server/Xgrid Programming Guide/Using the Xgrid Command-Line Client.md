---
title: Xgrid Programming Guide
apple_id: TP40006246
resource_type: Guide
platform: macOS
topic: Performance
technology: XgridFoundation
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/MacOSXServer/Conceptual/Xgrid_Programming_Guide/Usingthexgridcommandlineclient/Usingthexgridcommandlineclient.html
archived_at: '2026-07-15T08:16:48.250646Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xgrid Programming Guide](Introduction.md)


[Next](Building%20and%20Running%20GridSample.md)[Previous](Getting%20Started%20with%20Xgrid.md)

# Using the Xgrid Command-Line Client

Mac OS X version 10.4 and later includes the `xgrid` command-line utility. For some applications, the `xgrid` command-line tool is all the client software you need. In any event, you should become familiar with it to get a better understanding of Xgrid before writing an Xgrid-enabled client application.

The `xgrid` command-line utility is an Xgrid client. You can submit a job to a controller by typing xgrid followed by the controller’s host name and a job specification.

The job specification includes the name and path of an executable file, such as an application or a shell script, and any arguments to pass to the executable file.

You have the option of supplying an input file or a directory of files. If you supply an input directory, it is copied to each agent and becomes the working directory for the executable file.

You also have the option of specifying an output file or directory.

As each agent completes its task, the standard output and error streams are returned to the controller. You can pipe these streams to files or direct them to the output and error streams of the shell that submitted the job. You can also retrieve any other files created in the agent’s working directory during job execution. These files are returned to the output directory specified when the job is submitted.

If you type `man xgrid` from within the Terminal application, you see an illustration of the syntax for the command-line tool. The first few lines are shown in [Listing 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpinedanjnknltc).

__Listing 3-1__  Excerpt from the xgrid man page

```
SYNOPSIS
        xgrid [-h[ostname] hostname] [-auth { Password | Kerberos }] [-p[assword] password]
        xgrid -job run [-gid grid-identifier] [-si stdin] [-in indir] [-so stdout] [-se stderr] [-out outdir]
        [-email email-address]
       cmd [arg1 [...]]
       xgrid -job submit [-gid grid-identifier] [-si stdin] [-in indir] [-dids jobid [, jobid]*]
       [-email email-address]
       cmd [arg1 [...]]
```

The first parameter is `-h`, followed by the host name or IP address of the controller.

Example: `xgrid -h localhost`

You can optionally include a method of authentication and a password.

The next parameter of interest is the job specification. You can either run a job synchronously, by passing `-job run`, or submit a job for asynchronous execution by passing `-job submit`. In either case, you must then specify a grid, and can optionally redirect the standard input and output.

If you submit a job asynchronously, rather than running it synchronously, you can include an email address to be notified when the job terminates.

Here’s a very simple example that runs the `cal` program using a controller on the local host:

__Listing 3-2__  Running a job synchronously

```
xgrid -h localhost -job run /usr/bin/cal 2007
```

By specifying the full path, you prevent the executable file from being copied to the agent. Instead, it is run in place at the specified path location. No working directory is created.

By specifying `run` instead of `submit`, you tell `xgrid` to execute the command synchronously. The command line returns nothing until the job is complete.

Since the optional input and output specifications have been omitted, standard output is used for the results.

Now let’s look at a more complex example. It submits the file `myscript` with a group of files in an input directory. An email address is passed that will be used to notify someone at every job state change. The results are saved in files in an output directory, then the job is deleted:

__Listing 3-3__  Submitting a job asynchronously

```shell
$ xgrid -job submit -in ~/data/working -email somebody@apple.com myscript param1 param2
          { jobIdentifier = 27; }
          $ xgrid -job results -id 27 -so job.out -se job.err -out job-outdir
           $ xgrid -job delete -id 27
```

In this example, `xgrid` is told to execute the job asynchronously by passing `submit` instead of `run`.

Use the `-in` parameter to pass an input directory. This directory is copied to each agent and becomes the working directory on the agent’s host computer. You can include anything needed in the working directory, such as additonal input files, libraries, and executables. The executable file is run in this directory.

Next, specify the script to run, along with any input parameters. This completes the first line of input.

A job identifier is returned.

The next line of the example uses the job identifier to assign file names for the standard output, standard error, and job output for this particular job.

The last line deletes the job.

Here’s how to submit a batch job, consisting of multiple tasks. If enough agents are available, all of the tasks are performed simultaneously. Otherwise, each available agent is assigned a task and the first agent to finish is assigned another task, and so on until all the tasks have been completed.

To submit a batch job, you must include a property list file, describing each task to be performed. The `man` page for `xgrid` describes the structure of the property list file, but here’s a helpful shortcut—submit each individual task as its own job initially, and let `xgrid` generate the property list file for you. When the task completes, you can retrieve the property list file. You can edit the list to modify a task, duplicating it as necessary, or concatenate the property list files of several tasks into one batch.

For example, if you submit the `cal` program as a job, it looks like this:

```
xgrid -job submit /usr/bin/cal  6 2007
```

The `xgrid` command returns a job ID. When the job completes, you can use the job identifier to retrieve the complete job specification, including the property list:

```
xgrid -job specification -id n
{
    jobSpecification = {
        applicationIdentifier = "com.apple.xgrid.cli";
        inputFiles = {};
        name = "/usr/bin/cal";
        submissionIdentifier = abc;
        taskSpecifications = {
            0 = {arguments = (6, 2007); command = "/usr/bin/cal"; };
       };
   };
}
```

Copy the returned job specification and save it using the `.plist` file suffix. You can then submit the file to Xgrid as part of a batch job specification. If the example above were named `batch.plist`, you could submit the job like this:

```
xgrid -job batch batch.plist
```

Before going any further with Xgrid programming, try breaking up your job into executable tasks and submitting them using the `xgrid` command-line utility. The experience will provide a great deal of useful information to you about how to plan and execute your program.

[Next](Building%20and%20Running%20GridSample.md)[Previous](Getting%20Started%20with%20Xgrid.md)

