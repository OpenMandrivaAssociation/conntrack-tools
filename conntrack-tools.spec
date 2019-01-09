%define		_disable_ld_no_undefined 1
Summary:	Userspace tools for interacting with the Connection Tracking System
Name:		conntrack-tools
Version:	1.4.5
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://www.netfilter.org/projects/conntrack-tools/index.html
Source0:	http://netfilter.org/projects/conntrack-tools/files/%{name}-%{version}.tar.bz2
Source1:	http://netfilter.org/projects/conntrack-tools/files/%{name}-%{version}.tar.bz2.sig
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	pkgconfig(libmnl) >= 1.0.0
BuildRequires:	pkgconfig(libnetfilter_conntrack) >= 1.0.1
BuildRequires:	pkgconfig(libnetfilter_cttimeout) >= 1.0.0
BuildRequires:	pkgconfig(libnfnetlink) >= 1.0.0
BuildRequires:	pkgconfig(libnetfilter_queue) >= 1.0.2
BuildRequires:	pkgconfig(libnetfilter_cthelper) >= 1.0.0
BuildRequires:	pkgconfig(libtirpc)

%description
The conntrack-tools are a set of tools targeted at system administrators.
They are conntrack, the userspace command line interface, and conntrackd,
the userspace daemon. The tool conntrack provides a full featured interface
that has replaced the old procfs interface. Using conntrack, you can view and
manage the in-kernel connection tracking state table from userspace. On the
other hand, conntrackd covers the specific aspects of stateful firewalls to
enable highly available scenarios, and can be used as statistics collector as
well.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS TODO doc/stats/conntrackd.conf
%{_sbindir}/conntrack
%{_sbindir}/conntrackd
%{_sbindir}/nfct
%{_libdir}/%{name}
%{_mandir}/man8/conntrack.8*
%{_mandir}/man8/conntrackd.8*
%{_mandir}/man8/nfct.8*
%{_mandir}/man5/conntrackd.conf.5.*
