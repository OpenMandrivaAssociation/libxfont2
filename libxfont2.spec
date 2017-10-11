%define major 2
%define libname %mklibname xfont2 %{major}
%define devname %mklibname xfont2 -d

Summary:	X font Library
Name:		libxfont2
Version:	2.0.2
Release:	1
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfont2-%{version}.tar.bz2
BuildRequires:	bzip2-devel
BuildRequires:	pkgconfig(fontenc)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xtrans)

%description
X font Library.

%package -n %{libname}
Summary:	X font Library
Group:		Development/X11
Provides:	%{name} = %{EVRD}

%description -n %{libname}
X font Library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{EVRD}
Provides:	libxfont2-devel = %{EVRD}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXfont2-%{version}
%apply_patches

%build
%configure \
	--disable-static \
	--with-bzip2 \
	--without-fop

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXfont2.so.%{major}*

%files -n %{devname}
%{_libdir}/libXfont2.so
%{_libdir}/pkgconfig/xfont2.pc
%{_includedir}/X11/fonts/libxfont2.h

