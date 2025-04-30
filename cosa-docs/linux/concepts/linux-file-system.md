# Linux File System

Let's explore these Linux directories and relevant commands for retrieving information.  I'll focus on commands that provide insightful data for system administrators, security professionals, or forensic investigators, rather than basic navigation commands like `ls`.

## `/boot` (Boot Loader and Kernel Information)

* `uname -r`: Displays the currently running kernel version.  (Scenario: System update verification)

* `cat /boot/config-$(uname -r)`: Shows the kernel configuration. (Scenario: Troubleshooting hardware or driver issues)

* `ls /boot/grub` (or `ls /boot/efi` for UEFI systems): Lists boot loader files. (Scenario: Recovering from boot problems)

## `/bin` (Essential User Binaries)

* `which ls`: Shows the full path of the `ls` command. (Scenario: Ensuring correct binary execution)

* `file /bin/ls`: Displays file type information.  (Scenario: Identify binary types)

## `/sbin` (System Binaries - Administrator)

* `which shutdown`: Locates the shutdown command. (Scenario: Verifying command paths)

* `file /sbin/shutdown`:  Shows file information for the shutdown command.

## `/etc` (Configuration Files)

* `cat /etc/hostname`: Displays the system's hostname. (Scenario: Network configuration)

* `cat /etc/passwd`: Lists user accounts (though `getent passwd` is generally preferred). (Scenario: User management)

* `cat /etc/shadow`:  Contains encrypted passwords (requires root privileges and should be handled carefully). (Scenario: Password management – rarely accessed directly)

* `cat /etc/network/interfaces` (or relevant network config files):  Displays network configuration.  (Scenario: Network troubleshooting)

## `/root` (Root User's Home Directory)

* `ls -la /root`: Lists all files and directories in the root user's home directory. (Scenario: Investigating root user activity)

## `/home` (User Home Directories)

* `ls -l /home`: Lists user home directories. (Scenario: User management)

* `find /home -user username -type f -mtime -7`: Finds files modified by a user in the last 7 days. (Scenario: Track user activity)

## `/media` (Mount Point for Removable Media)

* `lsblk`:  Shows block devices and mount points, including removable media mounted under `/media`. (Scenario: Identify connected devices)

## `/mnt` (Temporary Mount Point)

* Similar to `/media`, check for mounted devices using `lsblk`. (Scenario: Identify manually mounted file systems)

## `/tmp` (Temporary Files)

* `ls -l /tmp`: Lists temporary files.  (Scenario: Clean up temporary files)

## `/var` (Variable Data)

* `ls /var/log`: Lists log files. (Scenario: System troubleshooting and forensics)

* `dmesg`: Displays kernel ring buffer messages. (Scenario: Diagnose kernel issues)

## `/usr` (User Programs and Libraries)

* `ls /usr/bin`, `ls /usr/sbin`, `ls /usr/lib`: List binaries, system binaries, and libraries. (Scenario: Software management)

* `locate filename`:  Finds files by name within the `/usr` hierarchy (and other locations). (Scenario: Locate specific files)

## `/lib` (Shared Libraries)

* `ldconfig -p`: Lists shared libraries and their paths. (Scenario: System configuration and troubleshooting)

## `/opt` (Optional Software)

* `ls /opt`: Lists installed optional software packages. (Scenario: Manage third-party software)

## `/dev` (Device Files)

* `ls -l /dev`: Lists device files.  (Scenario: Hardware interaction and management)

## `/proc` (Process Information)

* `ps aux`:  Lists all running processes with detailed information. (Scenario: System monitoring and process management)

* `cat /proc/cpuinfo`: Displays CPU information. (Scenario: System information gathering)

* `cat /proc/meminfo`:  Displays memory usage information. (Scenario: Memory monitoring)

* `ls -l /proc/[PID]`:  Access process-specific information for a given Process ID (PID). (Scenario: Detailed process inspection)


## `/sys` (System Information)

* `ls /sys/module`: Lists loaded kernel modules. (Scenario: Kernel module management)

* `modinfo module_name`:  Displays information about a specific kernel module.  (Scenario: Kernel debugging)



This is a deeper dive into practical command usage within these directories, showcasing scenarios where this information becomes valuable.  Remember to adapt commands and paths as needed for your specific distribution and use case. The `man` command remains your best resource for in-depth information about any command. Using these commands effectively is crucial for anyone working with Linux systems, especially in administration, security, or forensic roles.
