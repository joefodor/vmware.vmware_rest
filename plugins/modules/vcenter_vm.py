#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: vcenter_vm
short_description: Creates a virtual machine from existing virtual machine files on
  storage.
description: Creates a virtual machine from existing virtual machine files on storage.
options:
  bios_uuid:
    description:
    - 128-bit SMBIOS UUID of a virtual machine represented as a hexadecimal string
      in "12345678-abcd-1234-cdef-123456789abc" format.
    type: str
  boot:
    description:
    - Boot configuration.
    - 'Valid attributes are:'
    - ' - C(type) (str): The {@name Type} defines the valid firmware types for a virtual
      machine.'
    - '   - Accepted values:'
    - '     - BIOS'
    - '     - EFI'
    - ' - C(efi_legacy_boot) (bool): Flag indicating whether to use EFI legacy boot
      mode.'
    - ' - C(network_protocol) (str): The {@name NetworkProtocol} defines the valid
      network boot protocols supported when booting a virtual machine with {@link
      Type#EFI} firmware over the network.'
    - '   - Accepted values:'
    - '     - IPV4'
    - '     - IPV6'
    - ' - C(delay) (int): Delay in milliseconds before beginning the firmware boot
      process when the virtual machine is powered on.  This delay may be used to provide
      a time window for users to connect to the virtual machine console and enter
      BIOS setup mode.'
    - ' - C(retry) (bool): Flag indicating whether the virtual machine should automatically
      retry the boot process after a failure.'
    - ' - C(retry_delay) (int): Delay in milliseconds before retrying the boot process
      after a failure; applicable only when {@link Info#retry} is true.'
    - ' - C(enter_setup_mode) (bool): Flag indicating whether the firmware boot process
      should automatically enter setup mode the next time the virtual machine boots.  Note
      that this flag will automatically be reset to false once the virtual machine
      enters setup mode.'
    type: dict
  boot_devices:
    description:
    - Boot device configuration.
    - 'Valid attributes are:'
    - ' - C(type) (str): The {@name Type} defines the valid device types that may
      be used as bootable devices.'
    - '   This key is required.'
    - '   - Accepted values:'
    - '     - CDROM'
    - '     - DISK'
    - '     - ETHERNET'
    - '     - FLOPPY'
    elements: dict
    type: list
  cdroms:
    description:
    - List of CD-ROMs.
    - 'Valid attributes are:'
    - ' - C(type) (str): The {@name HostBusAdapterType} defines the valid types of
      host bus adapters that may be used for attaching a Cdrom to a virtual machine.'
    - '   - Accepted values:'
    - '     - IDE'
    - '     - SATA'
    - ' - C(ide) (dict): Address for attaching the device to a virtual IDE adapter.'
    - '   - Accepted keys:'
    - '     - primary (boolean): Flag specifying whether the device should be attached
      to the primary or secondary IDE adapter of the virtual machine.'
    - '     - master (boolean): Flag specifying whether the device should be the master
      or slave device on the IDE adapter.'
    - ' - C(sata) (dict): Address for attaching the device to a virtual SATA adapter.'
    - '   - Accepted keys:'
    - '     - bus (integer): Bus number of the adapter to which the device should
      be attached.'
    - '     - unit (integer): Unit number of the device.'
    - ' - C(backing) (dict): Physical resource backing for the virtual CD-ROM device.'
    - '   - Accepted keys:'
    - '     - type (string): The {@name BackingType} defines the valid backing types
      for a virtual CD-ROM device.'
    - 'Accepted value for this field:'
    - '       - C(ISO_FILE)'
    - '       - C(HOST_DEVICE)'
    - '       - C(CLIENT_DEVICE)'
    - '     - iso_file (string): Path of the image file that should be used as the
      virtual CD-ROM device backing.'
    - '     - host_device (string): Name of the device that should be used as the
      virtual CD-ROM device backing.'
    - '     - device_access_type (string): The {@name DeviceAccessType} defines the
      valid device access types for a physical device packing of a virtual CD-ROM
      device.'
    - 'Accepted value for this field:'
    - '       - C(EMULATION)'
    - '       - C(PASSTHRU)'
    - '       - C(PASSTHRU_EXCLUSIVE)'
    - ' - C(start_connected) (bool): Flag indicating whether the virtual device should
      be connected whenever the virtual machine is powered on.'
    - ' - C(allow_guest_control) (bool): Flag indicating whether the guest can connect
      and disconnect the device.'
    elements: dict
    type: list
  cpu:
    description:
    - CPU configuration.
    - 'Valid attributes are:'
    - ' - C(count) (int): New number of CPU cores.  The number of CPU cores in the
      virtual machine must be a multiple of the number of cores per socket. The supported
      range of CPU counts is constrained by the configured guest operating system
      and virtual hardware version of the virtual machine. If the virtual machine
      is running, the number of CPU cores may only be increased if {@link Info#hotAddEnabled}
      is true, and may only be decreased if {@link Info#hotRemoveEnabled} is true.'
    - ' - C(cores_per_socket) (int): New number of CPU cores per socket.  The number
      of CPU cores in the virtual machine must be a multiple of the number of cores
      per socket.'
    - ' - C(hot_add_enabled) (bool): Flag indicating whether adding CPUs while the
      virtual machine is running is enabled. This field may only be modified if the
      virtual machine is powered off.'
    - ' - C(hot_remove_enabled) (bool): Flag indicating whether removing CPUs while
      the virtual machine is running is enabled. This field may only be modified if
      the virtual machine is powered off.'
    type: dict
  datastore:
    description:
    - Identifier of the datastore on which the virtual machine's configuration state
      is stored.
    type: str
  datastore_path:
    description:
    - Datastore path for the virtual machine's configuration file in the format "[datastore
      name] path".  For example "[storage1] Test-VM/Test-VM.vmx".
    type: str
  disconnect_all_nics:
    description:
    - Indicates whether all NICs on the destination virtual machine should be disconnected
      from the newtwork
    type: bool
  disks:
    description:
    - Individual disk relocation map.
    - 'Valid attributes are:'
    - ' - C(type) (str): The {@name HostBusAdapterType} defines the valid types of
      host bus adapters that may be used for attaching a virtual storage device to
      a virtual machine.'
    - '   - Accepted values:'
    - '     - IDE'
    - '     - SCSI'
    - '     - SATA'
    - ' - C(ide) (dict): Address for attaching the device to a virtual IDE adapter.'
    - '   - Accepted keys:'
    - '     - primary (boolean): Flag specifying whether the device should be attached
      to the primary or secondary IDE adapter of the virtual machine.'
    - '     - master (boolean): Flag specifying whether the device should be the master
      or slave device on the IDE adapter.'
    - ' - C(scsi) (dict): Address for attaching the device to a virtual SCSI adapter.'
    - '   - Accepted keys:'
    - '     - bus (integer): Bus number of the adapter to which the device should
      be attached.'
    - '     - unit (integer): Unit number of the device.'
    - ' - C(sata) (dict): Address for attaching the device to a virtual SATA adapter.'
    - '   - Accepted keys:'
    - '     - bus (integer): Bus number of the adapter to which the device should
      be attached.'
    - '     - unit (integer): Unit number of the device.'
    - ' - C(backing) (dict): Existing physical resource backing for the virtual disk.
      Exactly one of {@name #backing} or {@name #newVmdk} must be specified.'
    - '   - Accepted keys:'
    - '     - type (string): The {@name BackingType} defines the valid backing types
      for a virtual disk.'
    - 'Accepted value for this field:'
    - '       - C(VMDK_FILE)'
    - '     - vmdk_file (string): Path of the VMDK file backing the virtual disk.'
    - ' - C(new_vmdk) (dict): Specification for creating a new VMDK backing for the
      virtual disk.  Exactly one of {@name #backing} or {@name #newVmdk} must be specified.'
    - '   - Accepted keys:'
    - '     - name (string): Base name of the VMDK file.  The name should not include
      the ''.vmdk'' file extension.'
    - '     - capacity (integer): Capacity of the virtual disk backing in bytes.'
    - '     - storage_policy (object): The {@name StoragePolicySpec} {@term structure}
      contains information about the storage policy that is to be associated the with
      VMDK file.'
    elements: dict
    type: list
  disks_to_remove:
    description:
    - Set of Disks to Remove.
    elements: str
    type: list
  disks_to_update:
    description:
    - Map of Disks to Update.
    type: dict
  floppies:
    description:
    - List of floppy drives.
    - 'Valid attributes are:'
    - ' - C(backing) (dict): Physical resource backing for the virtual floppy drive.'
    - '   - Accepted keys:'
    - '     - type (string): The {@name BackingType} defines the valid backing types
      for a virtual floppy drive.'
    - 'Accepted value for this field:'
    - '       - C(IMAGE_FILE)'
    - '       - C(HOST_DEVICE)'
    - '       - C(CLIENT_DEVICE)'
    - '     - image_file (string): Path of the image file that should be used as the
      virtual floppy drive backing.'
    - '     - host_device (string): Name of the device that should be used as the
      virtual floppy drive backing.'
    - ' - C(start_connected) (bool): Flag indicating whether the virtual device should
      be connected whenever the virtual machine is powered on.'
    - ' - C(allow_guest_control) (bool): Flag indicating whether the guest can connect
      and disconnect the device.'
    elements: dict
    type: list
  guest_OS:
    choices:
    - AMAZONLINUX2_64
    - AMAZONLINUX3_64
    - ASIANUX_3
    - ASIANUX_3_64
    - ASIANUX_4
    - ASIANUX_4_64
    - ASIANUX_5_64
    - ASIANUX_7_64
    - ASIANUX_8_64
    - ASIANUX_9_64
    - CENTOS
    - CENTOS_6
    - CENTOS_64
    - CENTOS_6_64
    - CENTOS_7
    - CENTOS_7_64
    - CENTOS_8_64
    - CENTOS_9_64
    - COREOS_64
    - CRXPOD_1
    - DARWIN
    - DARWIN_10
    - DARWIN_10_64
    - DARWIN_11
    - DARWIN_11_64
    - DARWIN_12_64
    - DARWIN_13_64
    - DARWIN_14_64
    - DARWIN_15_64
    - DARWIN_16_64
    - DARWIN_17_64
    - DARWIN_18_64
    - DARWIN_19_64
    - DARWIN_20_64
    - DARWIN_21_64
    - DARWIN_64
    - DEBIAN_10
    - DEBIAN_10_64
    - DEBIAN_11
    - DEBIAN_11_64
    - DEBIAN_4
    - DEBIAN_4_64
    - DEBIAN_5
    - DEBIAN_5_64
    - DEBIAN_6
    - DEBIAN_6_64
    - DEBIAN_7
    - DEBIAN_7_64
    - DEBIAN_8
    - DEBIAN_8_64
    - DEBIAN_9
    - DEBIAN_9_64
    - DOS
    - ECOMSTATION
    - ECOMSTATION_2
    - FEDORA
    - FEDORA_64
    - FREEBSD
    - FREEBSD_11
    - FREEBSD_11_64
    - FREEBSD_12
    - FREEBSD_12_64
    - FREEBSD_13
    - FREEBSD_13_64
    - FREEBSD_64
    - GENERIC_LINUX
    - MANDRAKE
    - MANDRIVA
    - MANDRIVA_64
    - NETWARE_4
    - NETWARE_5
    - NETWARE_6
    - NLD_9
    - OES
    - OPENSERVER_5
    - OPENSERVER_6
    - OPENSUSE
    - OPENSUSE_64
    - ORACLE_LINUX
    - ORACLE_LINUX_6
    - ORACLE_LINUX_64
    - ORACLE_LINUX_6_64
    - ORACLE_LINUX_7
    - ORACLE_LINUX_7_64
    - ORACLE_LINUX_8_64
    - ORACLE_LINUX_9_64
    - OS2
    - OTHER
    - OTHER_24X_LINUX
    - OTHER_24X_LINUX_64
    - OTHER_26X_LINUX
    - OTHER_26X_LINUX_64
    - OTHER_3X_LINUX
    - OTHER_3X_LINUX_64
    - OTHER_4X_LINUX
    - OTHER_4X_LINUX_64
    - OTHER_5X_LINUX
    - OTHER_5X_LINUX_64
    - OTHER_64
    - OTHER_LINUX
    - OTHER_LINUX_64
    - REDHAT
    - RHEL_2
    - RHEL_3
    - RHEL_3_64
    - RHEL_4
    - RHEL_4_64
    - RHEL_5
    - RHEL_5_64
    - RHEL_6
    - RHEL_6_64
    - RHEL_7
    - RHEL_7_64
    - RHEL_8_64
    - RHEL_9_64
    - SJDS
    - SLES
    - SLES_10
    - SLES_10_64
    - SLES_11
    - SLES_11_64
    - SLES_12
    - SLES_12_64
    - SLES_15_64
    - SLES_16_64
    - SLES_64
    - SOLARIS_10
    - SOLARIS_10_64
    - SOLARIS_11_64
    - SOLARIS_6
    - SOLARIS_7
    - SOLARIS_8
    - SOLARIS_9
    - SUSE
    - SUSE_64
    - TURBO_LINUX
    - TURBO_LINUX_64
    - UBUNTU
    - UBUNTU_64
    - UNIXWARE_7
    - VMKERNEL
    - VMKERNEL_5
    - VMKERNEL_6
    - VMKERNEL_65
    - VMKERNEL_7
    - VMWARE_PHOTON_64
    - WINDOWS_7
    - WINDOWS_7_64
    - WINDOWS_7_SERVER_64
    - WINDOWS_8
    - WINDOWS_8_64
    - WINDOWS_8_SERVER_64
    - WINDOWS_9
    - WINDOWS_9_64
    - WINDOWS_9_SERVER_64
    - WINDOWS_HYPERV
    - WINDOWS_SERVER_2019
    - WINDOWS_SERVER_2021
    - WIN_2000_ADV_SERV
    - WIN_2000_PRO
    - WIN_2000_SERV
    - WIN_31
    - WIN_95
    - WIN_98
    - WIN_LONGHORN
    - WIN_LONGHORN_64
    - WIN_ME
    - WIN_NET_BUSINESS
    - WIN_NET_DATACENTER
    - WIN_NET_DATACENTER_64
    - WIN_NET_ENTERPRISE
    - WIN_NET_ENTERPRISE_64
    - WIN_NET_STANDARD
    - WIN_NET_STANDARD_64
    - WIN_NET_WEB
    - WIN_NT
    - WIN_VISTA
    - WIN_VISTA_64
    - WIN_XP_HOME
    - WIN_XP_PRO
    - WIN_XP_PRO_64
    description:
    - The {@name GuestOS} defines the valid guest operating system types used for
      configuring a virtual machine. Required with I(state=['present'])
    type: str
  guest_customization_spec:
    description:
    - Guest customization spec to apply to the virtual machine after the virtual machine
      is deployed.
    - 'Valid attributes are:'
    - ' - C(name) (str): Name of the customization specification.'
    type: dict
  hardware_version:
    choices:
    - VMX_03
    - VMX_04
    - VMX_06
    - VMX_07
    - VMX_08
    - VMX_09
    - VMX_10
    - VMX_11
    - VMX_12
    - VMX_13
    - VMX_14
    - VMX_15
    - VMX_16
    - VMX_17
    - VMX_18
    - VMX_19
    description:
    - The {@name Version} defines the valid virtual hardware versions for a virtual
      machine. See https://kb.vmware.com/s/article/1003746 (Virtual machine hardware
      versions (1003746)).
    type: str
  memory:
    description:
    - Memory configuration.
    - 'Valid attributes are:'
    - ' - C(size_MiB) (int): New memory size in mebibytes. The supported range of
      memory sizes is constrained by the configured guest operating system and virtual
      hardware version of the virtual machine. If the virtual machine is running,
      this value may only be changed if {@link Info#hotAddEnabled} is true, and the
      new memory size must satisfy the constraints specified by {@link Info#hotAddIncrementSizeMiB}
      and {@link Info#hotAddLimitMiB}.'
    - ' - C(hot_add_enabled) (bool): Flag indicating whether adding memory while the
      virtual machine is running should be enabled. Some guest operating systems may
      consume more resources or perform less efficiently when they run on hardware
      that supports adding memory while the machine is running. This field may only
      be modified if the virtual machine is not powered on.'
    type: dict
  name:
    description:
    - Name of the new virtual machine.
    type: str
  nics:
    description:
    - List of Ethernet adapters.
    - 'Valid attributes are:'
    - ' - C(type) (str): The {@name EmulationType} defines the valid emulation types
      for a virtual Ethernet adapter.'
    - '   - Accepted values:'
    - '     - E1000'
    - '     - E1000E'
    - '     - PCNET32'
    - '     - VMXNET'
    - '     - VMXNET2'
    - '     - VMXNET3'
    - ' - C(upt_compatibility_enabled) (bool): Flag indicating whether Universal Pass-Through
      (UPT) compatibility is enabled on this virtual Ethernet adapter.'
    - ' - C(mac_type) (str): The {@name MacAddressType} defines the valid MAC address
      origins for a virtual Ethernet adapter.'
    - '   - Accepted values:'
    - '     - MANUAL'
    - '     - GENERATED'
    - '     - ASSIGNED'
    - ' - C(mac_address) (str): MAC address.'
    - ' - C(pci_slot_number) (int): Address of the virtual Ethernet adapter on the
      PCI bus.  If the PCI address is invalid, the server will change when it the
      VM is started or as the device is hot added.'
    - ' - C(wake_on_lan_enabled) (bool): Flag indicating whether wake-on-LAN is enabled
      on this virtual Ethernet adapter.'
    - ' - C(backing) (dict): Physical resource backing for the virtual Ethernet adapter.'
    - '   - Accepted keys:'
    - '     - type (string): The {@name BackingType} defines the valid backing types
      for a virtual Ethernet adapter.'
    - 'Accepted value for this field:'
    - '       - C(STANDARD_PORTGROUP)'
    - '       - C(HOST_DEVICE)'
    - '       - C(DISTRIBUTED_PORTGROUP)'
    - '       - C(OPAQUE_NETWORK)'
    - '     - network (string): Identifier of the network that backs the virtual Ethernet
      adapter.'
    - '     - distributed_port (string): Key of the distributed virtual port that
      backs the virtual Ethernet adapter.  Depending on the type of the Portgroup,
      the port may be specified using this field. If the portgroup type is early-binding
      (also known as static), a port is assigned when the Ethernet adapter is configured
      to use the port. The port may be either automatically or specifically assigned
      based on the value of this field. If the portgroup type is ephemeral, the port
      is created and assigned to a virtual machine when it is powered on and the Ethernet
      adapter is connected.  This field cannot be specified as no free ports exist
      before use.'
    - ' - C(start_connected) (bool): Flag indicating whether the virtual device should
      be connected whenever the virtual machine is powered on.'
    - ' - C(allow_guest_control) (bool): Flag indicating whether the guest can connect
      and disconnect the device.'
    elements: dict
    type: list
  nics_to_update:
    description:
    - Map of NICs to update.
    type: dict
  parallel_ports:
    description:
    - List of parallel ports.
    - 'Valid attributes are:'
    - ' - C(backing) (dict): Physical resource backing for the virtual parallel port.'
    - '   - Accepted keys:'
    - '     - type (string): The {@name BackingType} defines the valid backing types
      for a virtual parallel port.'
    - 'Accepted value for this field:'
    - '       - C(FILE)'
    - '       - C(HOST_DEVICE)'
    - '     - file (string): Path of the file that should be used as the virtual parallel
      port backing.'
    - '     - host_device (string): Name of the device that should be used as the
      virtual parallel port backing.'
    - ' - C(start_connected) (bool): Flag indicating whether the virtual device should
      be connected whenever the virtual machine is powered on.'
    - ' - C(allow_guest_control) (bool): Flag indicating whether the guest can connect
      and disconnect the device.'
    elements: dict
    type: list
  parallel_ports_to_update:
    description:
    - Map of parallel ports to Update.
    type: dict
  path:
    description:
    - 'Path to the virtual machine''s configuration file on the datastore corresponding
      to {@link #datastore).'
    type: str
  placement:
    description:
    - Virtual machine placement information.
    - 'Valid attributes are:'
    - ' - C(folder) (str): Virtual machine folder into which the virtual machine should
      be placed.'
    - ' - C(resource_pool) (str): Resource pool into which the virtual machine should
      be placed.'
    - ' - C(host) (str): Host onto which the virtual machine should be placed. If
      {@name #host} and {@name #resourcePool} are both specified, {@name #resourcePool}
      must belong to {@name #host}. If {@name #host} and {@name #cluster} are both
      specified, {@name #host} must be a member of {@name #cluster}.'
    - ' - C(cluster) (str): Cluster into which the virtual machine should be placed.
      If {@name #cluster} and {@name #resourcePool} are both specified, {@name #resourcePool}
      must belong to {@name #cluster}. If {@name #cluster} and {@name #host} are both
      specified, {@name #host} must be a member of {@name #cluster}.'
    - ' - C(datastore) (str): Datastore on which the virtual machine''s configuration
      state should be stored.  This datastore will also be used for any virtual disks
      that are created as part of the virtual machine creation operation.'
    type: dict
  power_on:
    description:
    - 'Attempt to perform a {@link #powerOn} after clone.'
    type: bool
  sata_adapters:
    description:
    - List of SATA adapters.
    - 'Valid attributes are:'
    - ' - C(type) (str): The {@name Type} defines the valid emulation types for a
      virtual SATA adapter.'
    - '   - Accepted values:'
    - '     - AHCI'
    - ' - C(bus) (int): SATA bus number.'
    - ' - C(pci_slot_number) (int): Address of the SATA adapter on the PCI bus.'
    elements: dict
    type: list
  scsi_adapters:
    description:
    - List of SCSI adapters.
    - 'Valid attributes are:'
    - ' - C(type) (str): The {@name Type} defines the valid emulation types for a
      virtual SCSI adapter.'
    - '   - Accepted values:'
    - '     - BUSLOGIC'
    - '     - LSILOGIC'
    - '     - LSILOGICSAS'
    - '     - PVSCSI'
    - ' - C(bus) (int): SCSI bus number.'
    - ' - C(pci_slot_number) (int): Address of the SCSI adapter on the PCI bus.  If
      the PCI address is invalid, the server will change it when the VM is started
      or as the device is hot added.'
    - ' - C(sharing) (str): The {@name Sharing} defines the valid bus sharing modes
      for a virtual SCSI adapter.'
    - '   - Accepted values:'
    - '     - NONE'
    - '     - VIRTUAL'
    - '     - PHYSICAL'
    elements: dict
    type: list
  serial_ports:
    description:
    - List of serial ports.
    - 'Valid attributes are:'
    - ' - C(yield_on_poll) (bool): CPU yield behavior. If set to true, the virtual
      machine will periodically relinquish the processor if its sole task is polling
      the virtual serial port. The amount of time it takes to regain the processor
      will depend on the degree of other virtual machine activity on the host.'
    - ' - C(backing) (dict): Physical resource backing for the virtual serial port.'
    - '   - Accepted keys:'
    - '     - type (string): The {@name BackingType} defines the valid backing types
      for a virtual serial port.'
    - 'Accepted value for this field:'
    - '       - C(FILE)'
    - '       - C(HOST_DEVICE)'
    - '       - C(PIPE_SERVER)'
    - '       - C(PIPE_CLIENT)'
    - '       - C(NETWORK_SERVER)'
    - '       - C(NETWORK_CLIENT)'
    - '     - file (string): Path of the file backing the virtual serial port.'
    - '     - host_device (string): Name of the device backing the virtual serial
      port. <p>'
    - '     - pipe (string): Name of the pipe backing the virtual serial port.'
    - '     - no_rx_loss (boolean): Flag that enables optimized data transfer over
      the pipe. When the value is true, the host buffers data to prevent data overrun.  This
      allows the virtual machine to read all of the data transferred over the pipe
      with no data loss.'
    - '     - network_location (string): URI specifying the location of the network
      service backing the virtual serial port. <ul> <li>If {@link #type} is {@link
      BackingType#NETWORK_SERVER}, this field is the location used by clients to connect
      to this server.  The hostname part of the URI should either be empty or should
      specify the address of the host on which the virtual machine is running.</li>
      <li>If {@link #type} is {@link BackingType#NETWORK_CLIENT}, this field is the
      location used by the virtual machine to connect to the remote server.</li> </ul>'
    - '     - proxy (string): Proxy service that provides network access to the network
      backing.  If set, the virtual machine initiates a connection with the proxy
      service and forwards the traffic to the proxy.'
    - ' - C(start_connected) (bool): Flag indicating whether the virtual device should
      be connected whenever the virtual machine is powered on.'
    - ' - C(allow_guest_control) (bool): Flag indicating whether the guest can connect
      and disconnect the device.'
    elements: dict
    type: list
  serial_ports_to_update:
    description:
    - Map of serial ports to Update.
    type: dict
  source:
    description:
    - Virtual machine to InstantClone from. Required with I(state=['clone', 'instant_clone'])
    type: str
  state:
    choices:
    - absent
    - clone
    - instant_clone
    - present
    - register
    - relocate
    - unregister
    default: present
    description: []
    type: str
  storage_policy:
    description:
    - The {@name StoragePolicySpec} {@term structure} contains information about the
      storage policy that is to be associated with the virtual machine home (which
      contains the configuration and log files). Required with I(state=['present'])
    - 'Valid attributes are:'
    - ' - C(policy) (str): Identifier of the storage policy which should be associated
      with the virtual machine.'
    type: dict
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    - 'If the value is not specified in the task, the value of '
    - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
  vm:
    description:
    - Identifier of the virtual machine to be unregistered. Required with I(state=['absent',
      'relocate', 'unregister'])
    type: str
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 1.0.0
requirements:
- python >= 3.6
- aiohttp
"""

EXAMPLES = r"""
- name: Collect the list of the existing VM
  vmware.vmware_rest.vcenter_vm_info:
  register: existing_vms
  until: existing_vms is not failed
- name: Create a VM
  vmware.vmware_rest.vcenter_vm:
    placement:
      cluster: '{{ my_cluster_info.id }}'
      datastore: '{{ my_datastore.datastore }}'
      folder: '{{ my_virtual_machine_folder.folder }}'
      resource_pool: '{{ my_cluster_info.value.resource_pool }}'
    name: test_vm1
    guest_OS: DEBIAN_8_64
    hardware_version: VMX_11
    memory:
      hot_add_enabled: true
      size_MiB: 1024
- name: Delete some VM
  vmware.vmware_rest.vcenter_vm:
    state: absent
    vm: '{{ item.vm }}'
  with_items: '{{ existing_vms.value }}'
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Delete some VM
msg:
  description: Delete some VM
  returned: On success
  sample: All items completed
  type: str
results:
  description: Delete some VM
  returned: On success
  sample:
  - _ansible_item_label:
      cpu_count: 1
      memory_size_MiB: 1080
      name: test_vm1
      power_state: POWERED_ON
      vm: vm-1221
    _ansible_no_log: 0
    _debug_info:
      operation: delete
      status: 204
    ansible_loop_var: item
    changed: 1
    failed: 0
    invocation:
      module_args:
        bios_uuid: null
        boot: null
        boot_devices: null
        cdroms: null
        cpu: null
        datastore: null
        datastore_path: null
        disconnect_all_nics: null
        disks: null
        disks_to_remove: null
        disks_to_update: null
        floppies: null
        guest_OS: null
        guest_customization_spec: null
        hardware_version: null
        memory: null
        name: null
        nics: null
        nics_to_update: null
        parallel_ports: null
        parallel_ports_to_update: null
        path: null
        placement: null
        power_on: null
        sata_adapters: null
        scsi_adapters: null
        serial_ports: null
        serial_ports_to_update: null
        source: null
        state: absent
        storage_policy: null
        vcenter_hostname: vcenter.test
        vcenter_password: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
        vcenter_rest_log_file: null
        vcenter_username: administrator@vsphere.local
        vcenter_validate_certs: 'no'
        vm: vm-1221
    item:
      cpu_count: 1
      memory_size_MiB: 1080
      name: test_vm1
      power_state: POWERED_ON
      vm: vm-1221
    value: {}
  - _ansible_item_label:
      cpu_count: 1
      memory_size_MiB: 128
      name: vCLS (1)
      power_state: POWERED_OFF
      vm: vm-1223
    _ansible_no_log: 0
    _debug_info:
      operation: delete
      status: 204
    ansible_loop_var: item
    changed: 1
    failed: 0
    invocation:
      module_args:
        bios_uuid: null
        boot: null
        boot_devices: null
        cdroms: null
        cpu: null
        datastore: null
        datastore_path: null
        disconnect_all_nics: null
        disks: null
        disks_to_remove: null
        disks_to_update: null
        floppies: null
        guest_OS: null
        guest_customization_spec: null
        hardware_version: null
        memory: null
        name: null
        nics: null
        nics_to_update: null
        parallel_ports: null
        parallel_ports_to_update: null
        path: null
        placement: null
        power_on: null
        sata_adapters: null
        scsi_adapters: null
        serial_ports: null
        serial_ports_to_update: null
        source: null
        state: absent
        storage_policy: null
        vcenter_hostname: vcenter.test
        vcenter_password: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
        vcenter_rest_log_file: null
        vcenter_username: administrator@vsphere.local
        vcenter_validate_certs: 'no'
        vm: vm-1223
    item:
      cpu_count: 1
      memory_size_MiB: 128
      name: vCLS (1)
      power_state: POWERED_OFF
      vm: vm-1223
    value: {}
  type: list
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "create": {
        "query": {},
        "body": {
            "boot": "boot",
            "boot_devices": "boot_devices",
            "cdroms": "cdroms",
            "cpu": "cpu",
            "disks": "disks",
            "floppies": "floppies",
            "guest_OS": "guest_OS",
            "hardware_version": "hardware_version",
            "memory": "memory",
            "name": "name",
            "nics": "nics",
            "parallel_ports": "parallel_ports",
            "placement": "placement",
            "sata_adapters": "sata_adapters",
            "scsi_adapters": "scsi_adapters",
            "serial_ports": "serial_ports",
            "storage_policy": "storage_policy",
        },
        "path": {},
    },
    "list": {
        "query": {
            "clusters": "clusters",
            "datacenters": "datacenters",
            "folders": "folders",
            "hosts": "hosts",
            "names": "names",
            "power_states": "power_states",
            "resource_pools": "resource_pools",
            "vms": "vms",
        },
        "body": {},
        "path": {},
    },
    "get": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "delete": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "relocate": {
        "query": {},
        "body": {"disks": "disks", "placement": "placement"},
        "path": {"vm": "vm"},
    },
    "unregister": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "clone": {
        "query": {},
        "body": {
            "disks_to_remove": "disks_to_remove",
            "disks_to_update": "disks_to_update",
            "guest_customization_spec": "guest_customization_spec",
            "name": "name",
            "placement": "placement",
            "power_on": "power_on",
            "source": "source",
        },
        "path": {},
    },
    "instant_clone": {
        "query": {},
        "body": {
            "bios_uuid": "bios_uuid",
            "disconnect_all_nics": "disconnect_all_nics",
            "name": "name",
            "nics_to_update": "nics_to_update",
            "parallel_ports_to_update": "parallel_ports_to_update",
            "placement": "placement",
            "serial_ports_to_update": "serial_ports_to_update",
            "source": "source",
        },
        "path": {},
    },
    "register": {
        "query": {},
        "body": {
            "datastore": "datastore",
            "datastore_path": "datastore_path",
            "name": "name",
            "path": "path",
            "placement": "placement",
        },
        "path": {},
    },
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
    }

    argument_spec["bios_uuid"] = {"type": "str"}
    argument_spec["boot"] = {"type": "dict"}
    argument_spec["boot_devices"] = {"type": "list", "elements": "dict"}
    argument_spec["cdroms"] = {"type": "list", "elements": "dict"}
    argument_spec["cpu"] = {"type": "dict"}
    argument_spec["datastore"] = {"type": "str"}
    argument_spec["datastore_path"] = {"type": "str"}
    argument_spec["disconnect_all_nics"] = {"type": "bool"}
    argument_spec["disks"] = {"type": "list", "elements": "dict"}
    argument_spec["disks_to_remove"] = {"type": "list", "elements": "str"}
    argument_spec["disks_to_update"] = {"type": "dict"}
    argument_spec["floppies"] = {"type": "list", "elements": "dict"}
    argument_spec["guest_OS"] = {
        "type": "str",
        "choices": [
            "AMAZONLINUX2_64",
            "AMAZONLINUX3_64",
            "ASIANUX_3",
            "ASIANUX_3_64",
            "ASIANUX_4",
            "ASIANUX_4_64",
            "ASIANUX_5_64",
            "ASIANUX_7_64",
            "ASIANUX_8_64",
            "ASIANUX_9_64",
            "CENTOS",
            "CENTOS_6",
            "CENTOS_64",
            "CENTOS_6_64",
            "CENTOS_7",
            "CENTOS_7_64",
            "CENTOS_8_64",
            "CENTOS_9_64",
            "COREOS_64",
            "CRXPOD_1",
            "DARWIN",
            "DARWIN_10",
            "DARWIN_10_64",
            "DARWIN_11",
            "DARWIN_11_64",
            "DARWIN_12_64",
            "DARWIN_13_64",
            "DARWIN_14_64",
            "DARWIN_15_64",
            "DARWIN_16_64",
            "DARWIN_17_64",
            "DARWIN_18_64",
            "DARWIN_19_64",
            "DARWIN_20_64",
            "DARWIN_21_64",
            "DARWIN_64",
            "DEBIAN_10",
            "DEBIAN_10_64",
            "DEBIAN_11",
            "DEBIAN_11_64",
            "DEBIAN_4",
            "DEBIAN_4_64",
            "DEBIAN_5",
            "DEBIAN_5_64",
            "DEBIAN_6",
            "DEBIAN_6_64",
            "DEBIAN_7",
            "DEBIAN_7_64",
            "DEBIAN_8",
            "DEBIAN_8_64",
            "DEBIAN_9",
            "DEBIAN_9_64",
            "DOS",
            "ECOMSTATION",
            "ECOMSTATION_2",
            "FEDORA",
            "FEDORA_64",
            "FREEBSD",
            "FREEBSD_11",
            "FREEBSD_11_64",
            "FREEBSD_12",
            "FREEBSD_12_64",
            "FREEBSD_13",
            "FREEBSD_13_64",
            "FREEBSD_64",
            "GENERIC_LINUX",
            "MANDRAKE",
            "MANDRIVA",
            "MANDRIVA_64",
            "NETWARE_4",
            "NETWARE_5",
            "NETWARE_6",
            "NLD_9",
            "OES",
            "OPENSERVER_5",
            "OPENSERVER_6",
            "OPENSUSE",
            "OPENSUSE_64",
            "ORACLE_LINUX",
            "ORACLE_LINUX_6",
            "ORACLE_LINUX_64",
            "ORACLE_LINUX_6_64",
            "ORACLE_LINUX_7",
            "ORACLE_LINUX_7_64",
            "ORACLE_LINUX_8_64",
            "ORACLE_LINUX_9_64",
            "OS2",
            "OTHER",
            "OTHER_24X_LINUX",
            "OTHER_24X_LINUX_64",
            "OTHER_26X_LINUX",
            "OTHER_26X_LINUX_64",
            "OTHER_3X_LINUX",
            "OTHER_3X_LINUX_64",
            "OTHER_4X_LINUX",
            "OTHER_4X_LINUX_64",
            "OTHER_5X_LINUX",
            "OTHER_5X_LINUX_64",
            "OTHER_64",
            "OTHER_LINUX",
            "OTHER_LINUX_64",
            "REDHAT",
            "RHEL_2",
            "RHEL_3",
            "RHEL_3_64",
            "RHEL_4",
            "RHEL_4_64",
            "RHEL_5",
            "RHEL_5_64",
            "RHEL_6",
            "RHEL_6_64",
            "RHEL_7",
            "RHEL_7_64",
            "RHEL_8_64",
            "RHEL_9_64",
            "SJDS",
            "SLES",
            "SLES_10",
            "SLES_10_64",
            "SLES_11",
            "SLES_11_64",
            "SLES_12",
            "SLES_12_64",
            "SLES_15_64",
            "SLES_16_64",
            "SLES_64",
            "SOLARIS_10",
            "SOLARIS_10_64",
            "SOLARIS_11_64",
            "SOLARIS_6",
            "SOLARIS_7",
            "SOLARIS_8",
            "SOLARIS_9",
            "SUSE",
            "SUSE_64",
            "TURBO_LINUX",
            "TURBO_LINUX_64",
            "UBUNTU",
            "UBUNTU_64",
            "UNIXWARE_7",
            "VMKERNEL",
            "VMKERNEL_5",
            "VMKERNEL_6",
            "VMKERNEL_65",
            "VMKERNEL_7",
            "VMWARE_PHOTON_64",
            "WINDOWS_7",
            "WINDOWS_7_64",
            "WINDOWS_7_SERVER_64",
            "WINDOWS_8",
            "WINDOWS_8_64",
            "WINDOWS_8_SERVER_64",
            "WINDOWS_9",
            "WINDOWS_9_64",
            "WINDOWS_9_SERVER_64",
            "WINDOWS_HYPERV",
            "WINDOWS_SERVER_2019",
            "WINDOWS_SERVER_2021",
            "WIN_2000_ADV_SERV",
            "WIN_2000_PRO",
            "WIN_2000_SERV",
            "WIN_31",
            "WIN_95",
            "WIN_98",
            "WIN_LONGHORN",
            "WIN_LONGHORN_64",
            "WIN_ME",
            "WIN_NET_BUSINESS",
            "WIN_NET_DATACENTER",
            "WIN_NET_DATACENTER_64",
            "WIN_NET_ENTERPRISE",
            "WIN_NET_ENTERPRISE_64",
            "WIN_NET_STANDARD",
            "WIN_NET_STANDARD_64",
            "WIN_NET_WEB",
            "WIN_NT",
            "WIN_VISTA",
            "WIN_VISTA_64",
            "WIN_XP_HOME",
            "WIN_XP_PRO",
            "WIN_XP_PRO_64",
        ],
    }
    argument_spec["guest_customization_spec"] = {"type": "dict"}
    argument_spec["hardware_version"] = {
        "type": "str",
        "choices": [
            "VMX_03",
            "VMX_04",
            "VMX_06",
            "VMX_07",
            "VMX_08",
            "VMX_09",
            "VMX_10",
            "VMX_11",
            "VMX_12",
            "VMX_13",
            "VMX_14",
            "VMX_15",
            "VMX_16",
            "VMX_17",
            "VMX_18",
            "VMX_19",
        ],
    }
    argument_spec["memory"] = {"type": "dict"}
    argument_spec["name"] = {"type": "str"}
    argument_spec["nics"] = {"type": "list", "elements": "dict"}
    argument_spec["nics_to_update"] = {"type": "dict"}
    argument_spec["parallel_ports"] = {"type": "list", "elements": "dict"}
    argument_spec["parallel_ports_to_update"] = {"type": "dict"}
    argument_spec["path"] = {"type": "str"}
    argument_spec["placement"] = {"type": "dict"}
    argument_spec["power_on"] = {"type": "bool"}
    argument_spec["sata_adapters"] = {"type": "list", "elements": "dict"}
    argument_spec["scsi_adapters"] = {"type": "list", "elements": "dict"}
    argument_spec["serial_ports"] = {"type": "list", "elements": "dict"}
    argument_spec["serial_ports_to_update"] = {"type": "dict"}
    argument_spec["source"] = {"type": "str"}
    argument_spec["state"] = {
        "type": "str",
        "choices": [
            "absent",
            "clone",
            "instant_clone",
            "present",
            "register",
            "relocate",
            "unregister",
        ],
        "default": "present",
    }
    argument_spec["storage_policy"] = {"type": "dict"}
    argument_spec["vm"] = {"type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/vcenter/vm").format(**params)


async def entry_point(module, session):

    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _clone(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["clone"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["clone"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm?action=clone&vmw-task=true")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm?action=clone&vmw-task=true"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}
        return await update_changed_flag(_json, resp.status, "clone")


async def _create(params, session):

    if params["vm"]:
        _json = await get_device_info(session, build_url(params), params["vm"])
    else:
        _json = await exists(params, session, build_url(params), ["vm"])
    if _json:
        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}
        if "_update" in globals():
            params["vm"] = _json["id"]
            return await globals()["_update"](params, session)
        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = ("https://{vcenter_hostname}" "/api/vcenter/vm").format(**params)
    async with session.post(_url, json=payload) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}

        if resp.status in [200, 201]:
            if isinstance(_json, str):  # 7.0.2 and greater
                _id = _json  # TODO: fetch the object
            elif isinstance(_json, dict) and "value" not in _json:
                _id = list(_json["value"].values())[0]
            elif isinstance(_json, dict) and "value" in _json:
                _id = _json["value"]
            _json_device_info = await get_device_info(session, _url, _id)
            if _json_device_info:
                _json = _json_device_info

        return await update_changed_flag(_json, resp.status, "create")


async def _delete(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["delete"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["delete"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}").format(
        **params
    ) + gen_args(params, _in_query_parameters)
    async with session.delete(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


async def _instant_clone(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["instant_clone"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["instant_clone"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm?action=instant-clone")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm?action=instant-clone"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}
        return await update_changed_flag(_json, resp.status, "instant_clone")


async def _register(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["register"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["register"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm?action=register")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm?action=register"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}
        return await update_changed_flag(_json, resp.status, "register")


async def _relocate(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["relocate"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["relocate"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/vm/{vm}?action=relocate&vmw-task=true"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}?action=relocate&vmw-task=true"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}
        return await update_changed_flag(_json, resp.status, "relocate")


async def _unregister(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["unregister"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["unregister"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}?action=unregister")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}?action=unregister"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}
        return await update_changed_flag(_json, resp.status, "unregister")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
