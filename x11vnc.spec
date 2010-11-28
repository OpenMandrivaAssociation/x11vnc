Name:           x11vnc
Version:        0.9.12
Release:        %mkrel 1
Summary:        VNC server for the current X11 session
License:        GPL
Group:          System/X11
URL:            http://www.karlrunge.com/x11vnc/
Source:         http://downloads.sourceforge.net/sourceforge/libvncserver/%{name}-%{version}.tar.gz
BuildRequires:  libx11-devel
BuildRequires:  libxdamage-devel
BuildRequires:  libxext-devel
BuildRequires:  libxrandr-devel
BuildRequires:  libxtst-devel
BuildRequires:  libxinerama-devel
BuildRequires:  libxfixes-devel
BuildRequires:  openssl-devel
BuildRequires:  libvncserver-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
x11vnc is to X Window System what WinVNC is to Windows, i.e. a server
which serves the current X Window System desktop via RFB (VNC)
protocol to the user.

Based on the ideas of x0rfbserver and on LibVNCServer, it has evolved
into a versatile and performant while still easy to use program.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

rm -fr %buildroot%_includedir

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_mandir}/man1/x11vnc.1*
%{_bindir}/x11vnc
%{_datadir}/x11vnc/
%{_datadir}/applications/x11vnc.desktop
