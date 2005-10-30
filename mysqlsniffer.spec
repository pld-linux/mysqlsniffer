# TODO
# - program crashed quite instanty
Summary:	Dumps packets that are sent or received over a network interface
Summary(pl):	Zrzucanie pakietów wysy³anych lub otrzymywanych po interfejsie sieciowym
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

%description -l pl
mysqlsniffer to klon tcpdumpa do podgl±dania ruchu MySQL-a w sieci.
Jest napisany w C z u¿yciem biblioteki pcap. Wy³apuje i interpretuje
ruch MySQL-a w sieci TCP/IP.

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
