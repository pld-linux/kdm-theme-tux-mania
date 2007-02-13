
%define		_theme		Tux-Mania

Summary:	Tux-Mania KDM theme
Summary(pl.UTF-8):	Motyw KDM Tux-Mania
Name:		kdm-theme-%{_theme}
Version:	01
Release:	2
License:	GPL
Group:		X11/Amusements
Source0:	http://www.kde-look.org/content/files/22187-%{_theme}.tar.bz2
# Source0-md5:	bb3aa0083d349432f165f6d7eb7b62ba
URL:		http://www.kde-look.org/content/show.php?content=22187
Requires:	kdebase-desktop >= 9:3.2.0
Requires:	kdm >= 9:3.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%define		_tm	tux-mania

%description
Tux-Mania of KDM Theme.

%description -l pl.UTF-8
Motyw KDM Tux-Mania.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_tm}

install %{_theme}/*.{desktop,jpg,png,xml} $RPM_BUILD_ROOT%{_datadir}/apps/kdm/themes/%{_tm}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdm/themes/%{_tm}
