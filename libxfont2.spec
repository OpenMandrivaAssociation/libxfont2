%define major 2
%define libname %mklibname xfont2 %{major}
%define devname %mklibname xfont2 -d

Summary:	X font Library
Name:		libxfont2
Version:	2.0.8
Release:	2
Group:		Development/X11
License:	MIT
Url:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXfont2-%{version}.tar.xz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	pkgconfig(bzip2)
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
%autosetup -n libXfont2-2.0.8 -p1

%if %{cross_compiling}
# Host ldconfig via spec-helper cannot process riscv64 ELF and would
# drop the installed soname symlink.
%define dont_symlinks_libs 1
%endif

%build
%configure \
	--disable-static \
	--with-bzip2 \
	--without-fop

%make_build LIBTOOL=slibtool

%install
%make_install LIBTOOL=slibtool
# slibtool also installs an export-symbols archive as .a
rm -f %{buildroot}%{_libdir}/libXfont2.a

%files -n %{libname}
%{_libdir}/libXfont2.so.%{major}*

%files -n %{devname}
%{_libdir}/libXfont2.so
%{_libdir}/pkgconfig/xfont2.pc
%{_includedir}/X11/fonts/libxfont2.h
