Summary:	"SteampunK Powered Linux" KSplash theme
Name:		kde4-style-steampunk-ksplash
Version:	3.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://kde-look.org/content/show.php?content=142138
Source:		http://sites.google.com/site/binaryinspiration/download/SteampunK_KSplash3.tar.gz
Requires:	kdebase4-workspace >= 4.10
BuildRequires:	kde4-macros
BuildArch:	noarch

%description
This package contains the "SteampunK Powered Linux" theme for KSplash.

%files
%{_kde_appsdir}/ksplash/Themes/SteampunK

#----------------------------------------------------------------------------

%prep
%setup -q -c
find . -type f | xargs chmod 0644

%build
# nothing

%install
mkdir -p %{buildroot}/%{_kde_appsdir}/ksplash/Themes

cp -r SteampunK %{buildroot}%{_kde_appsdir}/ksplash/Themes/

