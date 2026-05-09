# What is Operating System?

For any system to be called Operating system, it needs CPU, RAM, Monitor, Keyboard, and Harddisk. These components doesn't make any system operating system, but in order to operating system run, it needs these hardware components on which it could *run* and *manage*.

To define the operating system, you can say that OS is an interface between **End-User** and **Hradware**. Though having an general defination for OS is impossible. Mostly we are using an apllication over the OS, application programs, used to communicate with the operating system.

- To tell more about the Operating system, you can say that there is interface between the **application software** and **hardware**.
- To be more specific, we can say Operating system is the control program that controls the application software running on the Operating system.
- Operating system is a **resource allocator** or say resource manager, which allocates hardware resources to the programs running over the operating system, **one-by-one**.

<br>

# What lies in CD/DVD IOS file?

- It is composed of three things:
  - **Kernel**, which is the core OS repoonsible for managing the CPU, I/O devices, and memory management
  - **System software** that involves the other softwares that are part of OS that makes an OS function, like providing System utilities softwares, Shell and Command Interpreter and all that makes OS perform different functionality.
  - **System Utilities** that manages the functions apart from that of the Kernel, menaing monitoring and system analysis (we use `htop` and `ps` cmds to inspect) and software package management (we use apt-get in ubuntu for example).

It containes the Core Operating sytem software, along with additional application software, and system utilities (installed by default with the ISO file). The Core operating system is also called **Kernel**, because eventually all the other are controlled by Kernel, meaning it controls application s/w and system utilities.

# OS is like Big Elephant

Every aspect of the operating system is true but in order to the look at it hardware perspective, it is resource allocator, if you are looking at it using the software, you say it is a application contoller, an every aspect of the operating system is true, becuase it has different agents working in differenet aspect.

### Functions of Operating System

The below are the different aspects from which OS can looked and studies, it involves:

- Process Management
- CPU scheduling 
- Memory Mangement
- File & IO Mangement
- Hardware Extraction
- User Interfacing
- Networking
- Security and Protection

Out of which the Compulsary functionality are the first five and rest is optional. 

*What is Process?* Any Program loaded into the memory is called Process. So all the programs we run are the processes. IPC (Inter-Process Communication) handles all the coomunication between the processes. There are various kinds of IPCs:
- One of them are **socket** which is used for network communication, where client is able to communicate with the server and are able to send and recieve data using socket APIs. 
- Another example of the IPC is **Pipes** where one process reads the data from a file and another process write the data to the file. FIFO is one of the types called method of **Named Pipes**, where data can be communicated to another machines also, meaning other OSes.

Thus this can be seen using `ps` cmd in Linux. This is another command used for getting the PIDs of the processes, as that it is used to see the running processes on the system.

*CPU Scheduler* does the scheduling of the Processes. THe OS manages what process should be put into the CPU for processing, for example there is **Round-Robin Algorithm**, **First Come First Serve Algorithm**.

*Memory Management* is done using the RAM, when you need to manage and load the process, every plot of memory is dicided in the memory management. Use `free` cmd or `kill` cmd.

*File IO & Management* is the mangement of files and folder within the operating system, as we use `ls`, `mv`, `mkdir`, and `rmdir` to perform ops on files.

*Hardware Extraction* is the part that is the OS ensuring what part of Hardware is to allocated to the processes. 

*User Interfacing* is the part which provide application programs that helps in dealing with the Hardware components of the machine, importantly our **CLI** through which are are able to perform valrious operations on files and the folders.

*Networking*, basically this layer takes care of the network connection, implementation of TCP/IP, routing, and network security. You can perform networking `ipconfig`, `netstat`, and `ip` commands to configure the network.

*Security and Protection*, is where the OS takes care of the user authentiation, access-control lists, and encyrption of data, this can be performed using the `chmod`, `chrown`, and `sudo` cmds that you might use to implement the security of OS.

# File Management

File is simple collection of data and metadata (information about data), but with the perspective of Operating system, it see it in data and meta data, one is data that contains the data (actual data), another is meta data that contains the information about the file, operating system sees what the file is about, *what kind information is stored in meta data?* 

- **name/path**, OS stores the data name and the path to the file
- **size**
- **timestamps**, OS stores the create, access, and modify actions 
- **permission** given tothe files, there are three types of permission, read, write, and executable, managed at three levels, user/owner, group, and others
- **types**
- **user/owner**
- **group**
- **link count**
- **data block information**

# File System

File systems organize files on a storage device.  When a file is created, its data is initially stored in a data block (typically 4KB, though this is configurable). Simultaneously, metadata describing the file is stored separately in a File Control Block (FCB).  If the file exceeds the capacity of a single data block, multiple blocks are allocated, and the FCB tracks their locations and the file's overall size.

This metadata management is centralized.  The Master File Table (MFT) is a crucial component, storing comprehensive information about the entire volume or partition.  This includes the volume label, total size, used/free space, and importantly, details about the location and size of data blocks allocated to each file.

A partition, often referred to as the boot sector, contains the bootstrap program and bootloader responsible for initiating the operating system's boot process.

In summary, a file system organizes files across a partition, encompassing the data blocks, the MFT (containing FCB-like information), the Volume Control Block (VBC) which holds partition and volume information, and the Boot Sector.

The Linux equivalent of these structures uses different terminology:  the FCB is analogous to an inode; the Master File Table to an inode list; the Volume Control Block to the superblock; and the Boot Sector to the boot block.  The common file system used in Linux is the Extended File System (ext).

# Basically Linux File System divide Partition in Four Sections 

Linux file systems, such as the widely used Extended File System (ext), employ a different naming convention compared to the more general FCB-based description.  While the underlying concepts remain similar, the terminology reflects a different implementation.

Instead of a File Control Block (FCB), Linux uses an **inode**.  An inode is a data structure containing metadata about a file, including its size, permissions, timestamps (creation, last access, last modification), and crucially, pointers to the data blocks where the file's contents reside.  It doesn't directly store the file's data itself; instead, it acts as a directory entry pointing to the actual data.

The **inode list**, analogous to the Master File Table, is not a single, explicitly named table but rather an implicit organization of inodes.  The file system maintains a structured way to locate and access these inodes, essentially providing a mapping between filenames and their corresponding inodes.  This mapping is often stored in directory structures on the file system itself.

The **superblock** in Linux serves the same function as the Volume Control Block (VBC). It contains crucial information about the entire file system, such as its size, block size, free space, and the location of various system structures within the file system.  It's a central control point for the file system's metadata.

Finally, the **boot block** is directly equivalent to the Boot Sector.  This block contains the boot loader, the small program responsible for initiating the boot process by loading the operating system kernel.


In short, the concepts are the same, but Linux uses a more sophisticated and efficient implementation under a different naming scheme. The use of inodes, for example, provides a more flexible and robust method of managing file metadata. The Extended File System (ext) family, including ext2, ext3, ext4, and later versions, builds upon these core principles to provide a reliable and performant file system for Linux.


# How Linux manages files?

Liux creates files in **Tree Like Structure**, all the files are manges in Tree data structure, aranging data in multiple array. It is called **Root File Structure**. Linux contains the **root** defined as **`/`**. All the data is organised within the root folder itself.

```
❯ ls /
afs  boot  etc   lib    media  opt   root  sbin  sys  usr
bin  dev   home  lib64  mnt    proc  run   srv   tmp  var
```

- **boot** dir - this contains the booting related information of the operating system, information of the kernel that id stored inside the boot. It also contains kernel config file.
- **bin** dir - stands for binary files, all the files are in binary, containing executables of all the existing commands. Think of the `ls` command, when you use `ls` command, the executbales of `ls` is stored in bin directory.
- **sbin** dir - there are command that are only executable by the administrators only, therefore other users cannot execute them, so all those admin cmds are inside the **sbin**. It is also called super user
- **etc** dir - all config files are kept, for example, user configuration files and netowrk config files etc., such as hostname related information, passwords related information etc.
- **root** dir - is for root user or super user, also called home directory of **super** user. All the files that downloaded by root user are saved and stoered here.
- **home** dir - contains all the regular users in the home directory, where repective data or files of the user is saved in respective directories, one user cannot make dir in other users directory.
- **media** dir - all the removable devices are saved here, such as hard disk, pendrives etc., to save the data inside those devices are saved in media directory.
- **mnt** dir - 
- **tmp** dir - data of this directory is tmporary directory, remember that the files in this directory will be removed if the system is shutdown. Only store such data that has to be stored or used temprory.
- **var** dir - variable data files are kept in var directory, used to maintain the log of the activities can be stored in the var directory. For example ther is `dmesg` show the kernel log messages ans these command are used to store the log messages. Check for the **var** directory to check out the logs to troubleshoot the system.
- **usr** dir - all users application data is stored in the usr directory, remember that there is difference as it stores the user application data.
  - bin
  - sbin
  - lib
  - share 
- **lib** dir - Lists shared libraries and their paths.
- **opt** - all the third party data goes to the opt directory, as those s/w not provided by the OS.
- **dev** dir - it has all device files, remember unlike media dir, it stores all the device files.
- **proc** dir - stores all the system processes and system related information, captures memory related information. All the information regarding teh process is stored inside the proc directory.
- **sys** dir - all kernel modules information is stored, as kernel doesn't do anything itself, so all those inforamtion about the modules are stored here.

There are certain commands associated to the directories, for example, if you need ceratin information regarding the user, you need to take follow ups with `/home` directory. Refer to [Linux File System](../concepts/linux-file-system.md) to understand more about it. 

The data for the **/dev**, **/proc**, and **/sys** is dynamically generated during the runtime and thereofore the data is dynamical in size is isn't stored on the hard disk. While the data within these directories isn't typically stored persistently on the hard drive in a way that `/home` is, the directories themselves exist and their contents are dynamically generated and updated throughout the system's operation.  

# Accessing Directories

In order to access the file you need to use the path to the file, the path to the file is a string that contains the path tot the file, for example `/proc/533`, meaning there is **root** -> **proc** -> **533**.

There ar etwo kinds of path, **absolute directory** and **relative direcotry**.

1. **Absolute directory** goes with `/` always, for example, `/home/ditiss/python/demos/demo2.py`
2. **Relative directory** goes with respective to the **current working directory**, for example, `python/demos/demos2.py`

There are two kinds one is GUI and CLI, that user-interface is called **Shell** and the commands are given using CLI, command prompt to interact with operating system.

1. **CLI** <br>
Windows - cmd.exe, powershell.exe <br>
Linux - bsh, bash, esh, ksh, zsh

2. **GUI** <br>
Windows - explorer.exe <br>
Linux - GNOME (GNU Network Object Modal Env), KDE (Kimman Desktop Env)


# Shell

Mostly the `bash` shell is used by default, called **Born Again shell**. You can open the shell using the GUI application called Terminal that uses CLI on in the backend.

- Use `echo $SHELL` to see the default shell your are using. Because the shell being used is `zsh` and it is stored in **bin**, which means it can be used by any user.
    ```
    bash-5.2$ echo $SHELL
    /bin/zsh
    ```
- Use `ls` *path* to see the directory within the path specified.
    ```
    bash-5.2$ ls /
    Applications	Users		cores		home		sbin		var
    Library		Volumes		dev		opt		tmp
    System		bin		etc		private		usr
    ```
You can also check the the proc directory, see there is **cpuinfo** and **meminfo**, now you can see that there are memory 

- You can check and change the date. Use `date` cmd along with options to change it.

    ```
    ❯ date
    Thu Sep 26 12:20:45 IST 2024
    ```
Go an explore different types of the options and **FORMAT** you can use in the commands.

- You can see the calender using `cal` cmd.

    ```
    ❯ cal
    September 2024     
    Su Mo Tu We Th Fr Sa  
    1  2  3  4  5  6  7  
    8  9 10 11 12 13 14  
    15 16 17 18 19 20 21  
    22 23 24 25 26 27 28  
    29 30                 
    ```

- Use `pwd` to see the current working direcotry. 

- Create multiple directories using `mkdir` *file1* *file2* *file3*.

- Use `-p` as option for creating the directories in the hierarchy within the directories.
    ```
    ❯ mkdir -p create/dir/within/the/dir
    ❯ ls
    create
    ❯ ls create/
    dir
    ❯ ls create/dir/
    within
    ❯ ls create/dir/within/
    the
    ```

- Use *Ctrl + L* in Windows and *Cmd + L* in the Mac for `clear`.

- Use `-R` for seeing the content within the directory recursivley.
    ```
    ❯ ls -R
    create

    ./create:
    dir

    ./create/dir:
    within

    ./create/dir/within:
    the

    ./create/dir/within/the:
    dir

    ./create/dir/within/the/dir:
    ```

- Create an empty file using the `touch` command.

- Use `cat` commands to **show** the contents of the file and **create** a file with content. 
    ```
    cat > file.txt 
    ❯ cat file.txt
    Testing DITISS-LINUX
    Sunbeam Information
    ```
    Remember if you tried using the command on the pre-existing file, then in that case the file content will be overidden. If you need to append the content, you can use `cat >> file.txt` meaning that you can append the data.

- Simply use `rm` to remove the file from the machine.

- Use `cp` *src*  to create a copy of the file as well to copy the file to the *path destination*, if you want to copy the direcotry to the directory, use the 

- Remember that using `mv` command you don't need `-R`

- Use `rmdir` along with the `-r` followed by the file name, if the directory is not empty.


The below are the convention that are followed in the Linux.

| | |
|-----------|-------------------|
|Hard Disk  | sda, sdb, sdc, ...|
|Partitions  | sda1, sda2, sda3, ...|

# What is kernel Ring Buffer?

The kernel ring buffer is a circular buffer in the Linux kernel's memory used to store system messages, primarily logging kernel events.  Think of it like a rotating log file – when the buffer fills up, new messages overwrite the oldest ones.  This ensures that the kernel always has a recent record of events, even if there's a continuous stream of messages.  Its circular nature prevents the need for constant file writing and management, making it efficient for recording many small messages that may not all be interesting to the user.  The size of the ring buffer is configurable, but the default size is often relatively small, meaning that crucial messages might get overwritten if the system is experiencing high levels of activity.

The `dmesg` command is a simple utility that displays the contents of the kernel ring buffer.  When you run `dmesg`, it reads and prints the messages stored in this buffer, providing a history of recent kernel events, including boot messages, driver loading information, warnings, and errors. This is invaluable for troubleshooting system problems, as it shows what the kernel was doing just before a crash or malfunction.  Various options allow filtering and formatting of the output, making it possible to extract specific information from the sometimes voluminous log.  For example, `dmesg | tail` shows only the most recent messages.
