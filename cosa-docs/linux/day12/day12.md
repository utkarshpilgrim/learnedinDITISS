# Storage

Storage is defined as the four parameter as given below:

- Types
- Partitioning
  - Physical volumes 
  - Logical volumes, it is what we called LVM (Logical Volume Mangment)
- Format/ Creating File System on disk
- Mounting

# Administrative Storage

Administrative storage refers to the dynamic and flexible storage choices that an adminstrator might make to ensure or resolve the storage requirement within the organisation. There can be traditional storage mediums that work well for partitioning and there can be Logical Volumes for the efficient storage management.

1. Mangement involes the management of disk, understaning hardware such as PATA (Prallel ATA), SATA (Serial ATA), and SCSI (Small Computer System Interface). It basically means how you can change or manipulate the storage options.
2. Sysadmins needs to know the hardware very well, because until you don't you won't be able to [understand the data](#understanding-storage).

Storage are multiple types, one is **electornic** medium, such as SSD, Flash Drives (containing USB sticks), these are called electronic medium, data gets stored in **resultant** currents. For example, SSDs nowadays.

The second type is called **magnetic** medium, for example, HDDs, here data is stored in magenetic poles, such as North pole and South pole. Thus, this means unlike the resultant current where there are either 0 or 1 representing the current, but here in magnetic disk, it is north pole and south pole, north pole represent the 0 and south pole represent the 1.

The third one is called **Polycarbonate** medium, for example, CD/DVD storage mediums. It has two parts **pit** (representing 1) and **land** (representing 0). The concept of pit and land is simple, they are unchangeable, once the CD is burned, there is no way of going back, and therefore you need to think before you go for the storage options.

*So, there are few consideration*, if you need performance you should consider the electronic medium such as SSDs. If you are going for the large storage, you should go for the HDDs, medium, thus it is for **Database** storage.

Network-based storage, such as NAS, SAN, and cloud technologies, may also be used.

# Understanding Storage

*Now we need to see multiple options for storing the data.* It could be **Capacity** or **Durability**, **bugdet** or **performance**. The hardware decision should be made based on the certain criteria. The certain criterias can be classified in different aspects. 

#### Aspects of storage

HDDs are inexpensive and budget friendly, and have good capacity to store the data. Thus, SDDs are expensive and do give good performance, then, USBs, they are used as the connection devices to connect different devices including storage devices. So there are different interface that allows you to store different kind of data.

|Interface|.extension|
|---------|----------|
|USB| Mostly uesd in Printers, Hard Drives|
|M.2| Used in Internal SSDs|
|SATA| HD/CD Drives |
|PATA| HD/CD Drives|
|Firewire| Cameras, iPods|
|eSATA| Express SATA: Way Faster|

# /dev

It contains all the device files and after the recognistion the linux gives names to the dev. This directory contains all the connected device information and devices can be classified as below.

|Devices||
|-|-|
|**dev/sda** | Any **HDD Driver**/**SDD Drivers** based or could be **SATA** based devices are mentioned as dev/sda, dev/sdb and so on.  |
|**dev/nvme0n1**| It is called **Non-volatile memory express**, any Non-volatile storage options such as modern SDDs are mentioned inside dev/nvme0n1, dev/nvme0n2 and so on.  |
|**dev/hda**| It is called the old-school hard drives that are very slow, uses magnetic disk and are very cheap |
|dev/vda| Called **Kernel-based Virtual Machine**, these are called KVM |
|dev/xvda| When Virtual Machines are running on the Xen, then xvda is used|

# Types of Storage Design

There are storage mediums such as storing data in File Storage, it must be scaled our rather thatn scaled down. It is also called Network File System and Service.\

Then there is block storage, these are stored and given in two methods, it is very quick an reliable, it is basically used in cloud storage, it is also called **NAS (Network Attached Network)**. 

Then there is Object storage, where the data is stored over the static data because it difficult to manage the storage your self, both of them are used on clud.

```
zram0           252:0    0  1.9G  0 disk [SWAP]
```

This is called the SWAP memory.

# Partition

Disk partitioning divides a physical hard drive into logical units called partitions.  These partitions appear as separate drives to the operating system (e.g., C:, D: in Windows).  Partitioning allows for organizing data, installing multiple operating systems, and separating system files from user data.  While drive letters are a Windows convention, other operating systems use different identification methods (e.g., `/dev/sda1`, `/dev/sdb2` in Linux).

The Master Boot Record (MBR) is a crucial data structure located in the very first sector of a hard drive (sector 0, often called the "boot sector"). It plays a critical role in the boot process. The MBR contains three key components:

1. **Boot Code (First 446 Bytes):** This code is executed by the BIOS (Basic Input/Output System) during startup.  Its primary function is to locate and load the operating system's bootloader (e.g., GRUB, LILO in Linux, NTLDR in older Windows versions).  The boot code is small and acts as an initial pointer to the larger, more complex bootloader, which resides elsewhere on the disk.  The term "bootloader" is sometimes used interchangeably with "boot code," but they are distinct: the boot code is a very small program within the MBR that hands off control to the bootloader.

2. **Partition Table (Next 64 Bytes):**  This table contains descriptive information about the primary partitions on the hard drive. For each partition, the table stores its starting and ending location (using Cylinder-Head-Sector (CHS) addressing in older systems or Logical Block Addressing (LBA) in modern systems), its size, and its type (e.g., bootable, extended).  The partition table *does not contain the actual data* of the partitions; it merely provides a map of their locations on the disk.

3. **MBR Signature (Final 2 Bytes):** The signature, `0x55AA` (or `AA55` depending on endianness), marks the end of the MBR and indicates to the BIOS that the MBR is valid. If the signature is missing or incorrect, the BIOS may assume the disk is not bootable.

**Limitations and Risks of MBR:**

* **Four Primary Partition Limit:** The MBR scheme allows for only four primary partitions. To overcome this limitation, one of the primary partitions can be designated as an "extended partition."  This extended partition can then be subdivided into multiple "logical partitions."
* **2 TB Size Limit:** The MBR uses 32-bit addressing for LBA, limiting the maximum addressable disk size to 2 Terabytes (TB).  Larger disks require the use of the GUID Partition Table (GPT) scheme.
* **Single Point of Failure:** Because all boot information resides in a single sector, the MBR is vulnerable to corruption or damage.  If the MBR is corrupted, the system may become unbootable.  Regular backups and recovery tools are important for mitigating this risk.

**GPT (GUID Partition Table):**

Modern systems often use GPT, which overcomes the limitations of MBR. GPT uses globally unique identifiers (GUIDs) for partitions and supports larger disk sizes and more than four primary partitions. GPT also includes redundancy and checksums for improved data integrity.

In summary, understanding the MBR structure, its function in the boot process, and its limitations is essential for anyone working with disk management and system administration.  The boot code, partition table, and signature within the MBR are critical components that enable the system to locate and load the operating system. While MBR has been largely superseded by GPT, understanding its principles remains valuable for working with older systems or troubleshooting boot issues.


 ## Managing Partitions and Mount Points

This document outlines the steps to create, format, and mount partitions on a 10GB hard drive (represented as `/dev/nvme0n2` in this example – adapt as needed for your specific device).

**1. Partitioning the Disk:**

Use `fdisk` (for MBR) or `gdisk` (for GPT – recommended) to create three partitions:

```bash
sudo fdisk /dev/nvme0n2   # Or sudo gdisk /dev/nvme0n2
```

Within the `fdisk` or `gdisk` utility:
* Use the `n` command to create new partitions.
* Specify the desired size for each partition (2GB, 3GB, and 5GB).
* Use the `w` command to write the partition table to the disk.



**2. Formatting the Partitions:**

Format each partition with the desired filesystem:

```bash
sudo mkfs.ext4 /dev/nvme0n2p1  # Format partition 1 with ext4
sudo mkfs.xfs /dev/nvme0n2p2   # Format partition 2 with xfs
sudo mkfs.ext4 /dev/nvme0n2p3  # Format partition 3 with ext4
```

**3. Creating Mount Points:**

Create directories that will serve as mount points for the partitions:

```bash
sudo mkdir /p1
sudo mkdir /p2
sudo mkdir /p3
```

**4. Mounting the Partitions:**

Mount each partition to its corresponding mount point:

```bash
sudo mount /dev/nvme0n2p1 /p1
sudo mount /dev/nvme0n2p2 /p2
sudo mount /dev/nvme0n2p3 /p3
```


**5. Verification:**

Use the `findmnt` command to verify that the partitions are mounted correctly:

```bash
sudo findmnt
```

This command will display information about mounted filesystems, including the device, mount point, filesystem type, and other details.

* **Device Names:**  Replace `/dev/nvme0n2` with the actual device name of your hard drive. Use `lsblk` to list block devices and identify the correct one.

* **Partition Numbers:** The partition numbers (`p1`, `p2`, `p3`) might vary depending on your existing partitioning scheme.  Verify with `lsblk`.

* **MBR vs. GPT:** Use `fdisk` for MBR disks and `gdisk` or `parted` for GPT disks.  GPT is recommended for modern systems.

* **Persistent Mounting:** To mount partitions automatically at boot, add entries to the `/etc/fstab` file. (Exercise caution when editing fstab, as incorrect entries can prevent your system from booting).

## Auto-Mounting with `/etc/fstab`

The `/etc/fstab` file (File System Table) controls how and when filesystems are mounted at boot time and on demand.  Adding entries to this file allows you to automatically mount partitions, network shares, or other devices without manual intervention. **Steps for Auto-Mounting:**

Edit `/etc/fstab`

```bash
sudo vim /etc/fstab 
```

Add an Entry (using tabs, not spaces). Each line in `/etc/fstab` represents a mount point.  The format is:

```
# add the following entry in the file
# please make sure, you are using tab not the spaces
# /dev/nvme0n2p1    /p1 ext4    defaults    0   0
# /dev/nvme0n2p2    /p2 xfs    defaults    0   0
# /dev/nvme0n2p3    /p3 ext4    defaults    0   0
```

Reload Systemd (or init system). This step is essential to make systemd aware of the changes to `/etc/fstab`.

```bash
sudo systemctl daemon-reload
```

Test and Verify.

```bash
sudo mount -a  # Mounts all entries in /etc/fstab
```

Once you are done with mounting, you can go and create files within the file mounted directory and check for the respective filesystem using `df -T /disk1/something.txt`.

# Auto-mounting using systemd

We need to create the unit file with the naming convention of suppose `/devices/disk1`, so we need to create a `.mount` file with **devices-disk1.mount** in path `/etc/systemd/system/`, otherwise it would not work.

```bash 
> bash vim /etc/systemd/system/devices-disk1.mount

[Unit]
Description="This is a test mount used to mount first partition"

[Mount]
What=/dev/nvme0n2p1
Where=/devices/disk1
Type=ext4

[Install]
WantedBy=multi-user.target
```

Next, reload the daemon service. 

```bash
> sudo systemctl daemon-reload
```

Next, we need to check the status of mount point and the status at the time should be inactive (dead). 

```bash 
> sudo systemctl status device-disk1.mount
> sudo systemctl start device-disk1.mount
# now the service should show active
> sudo systemctl status device-disk1.mount
> sudo systemctl enable device-disk1.mount
> sudo systemctl enable device-disk1.mount
```


# LVM 

Logical Volume Management is the concept of using the distinct hard drive, say 10GB each, but you can't create a 25GB of partition on the Hard Drives. Thus, LVM provides a better storage meangement and this enables you to create associated logical disk, not real, but you can utilize the storage of three different disk into **one** logical Storage. That is called **LVM**.

You can find the logical creation of the disk inside **/dev/mapper**.

Lets see the steps again, we are going to do the mounting 

### Physical Volume

```
nvme0n3         259:8    0   10G  0 disk
nvme0n4         259:9    0   10G  0 disk
```

Check the default Physical VOlume created at the time of booting

```
root@localhost:~# pvs
  PV             VG     Fmt  Attr PSize  PFree
  /dev/nvme0n1p3 fedora lvm2 a--  18.41g 3.41g
```

Now we need to create th physical voleume

```
root@localhost:~# sudo pvcreate /dev/nvme0n3
  Physical volume "/dev/nvme0n3" successfully created.
root@localhost:~# sudo pvcreate /dev/nvme0n4
  Physical volume "/dev/nvme0n4" successfully created.
```

You can also check for the information of the disk created

```
root@localhost:~# pvdisplay /dev/nvme0n3
  "/dev/nvme0n3" is a new physical volume of "10.00 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/nvme0n3
  VG Name               
  PV Size               10.00 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               0UwAuo-u7F5-pCxw-0iYl-pNhf-wekl-q46qJN
```

You can see that it is not part of any virtual group. Now we nee dto create the virtual group.

### Virtual Groups

We now need to see the existing virtual group.

```
root@localhost:~# vgs
  VG     #PV #LV #SN Attr   VSize  VFree
  fedora   1   1   0 wz--n- 18.41g 3.41g
```

lets create a new virtual group using two phyical volumes.

```
root@localhost:~# sudo vgcreate myvg /dev/nvme0n3 /dev/nvme0n4
  Volume group "myvg" successfully created
```

Now you can check if the vg got created or not

```
root@localhost:~# vgs
  VG     #PV #LV #SN Attr   VSize  VFree 
  fedora   1   1   0 wz--n- 18.41g  3.41g
  myvg     2   0   0 wz--n- 19.99g 19.99g
```

Now you can see the vg information using the `vgdisplay`.

```
VG Size               18.41 GiB
```

Now all that is left is the creation of logical volume. 

```
root@localhost:~# lvs
  LV   VG     Attr       LSize  Pool Origin Data%  Meta%  Move Log Cpy%Sync Convert
  root fedora -wi-ao---- 15.00g
```

We can create using the following commands.

```
root@localhost:~# lvcreate -n lv1 -L 15GB myvg
  Logical volume "lv1" created.
```

Now you can check whether the lv got created or not.

```
LV Path                /dev/myvg/lv1
```

Now how do you format this partition. 

```
mkfs.ext4 /dev/mapper/myvg-lv1 
```

Now you need to maas

### Logical Volume