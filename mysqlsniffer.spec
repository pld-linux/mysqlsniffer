Summary:	dumps packets that are sent or received over a network interface
Name:		mysqlsniffer
Version:	1.1
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://hackmysql.com/code/%{name}.tgz
# Source0-md5:	3db83ce9f8710d4226a373fff39a238f
URL:		http://hackmysql.com/mysqlsniffer
BuildRequires:	libpcap-devel >= 2:0.8.3-6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mysqlsniffer is a tcpdump clone for watching MySQL traffic on a
network. Coded in C using the pcap library, mysqlsniffer captures and
interprets MySQL traffic on a TCP/IP network.

%prep
%setup -q -c

%build
%{__cc} %{rpmcflags} %{rpmldflags} -Wall -lpcap -o mysqlsniffer mysqlsniffer.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install %{name} $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
