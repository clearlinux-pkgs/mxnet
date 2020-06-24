#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7273634B104F135F (ptrendx@apache.org)
#
Name     : mxnet
Version  : 1.6.0
Release  : 25
URL      : https://github.com/apache/incubator-mxnet/releases/download/1.6.0/apache-mxnet-src-1.6.0-incubating.tar.gz
Source0  : https://github.com/apache/incubator-mxnet/releases/download/1.6.0/apache-mxnet-src-1.6.0-incubating.tar.gz
Source1  : https://github.com/apache/incubator-mxnet/releases/download/1.6.0/apache-mxnet-src-1.6.0-incubating.tar.gz.asc
Summary  : A deep learning framework designed for both efficiency and flexibility
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSD-3-Clause-LBNL ICU Libpng MIT MPL-2.0 NCSA Unlicense Zlib libtiff
Requires: mxnet-license = %{version}-%{release}
Requires: mxnet-python = %{version}-%{release}
Requires: mxnet-python3 = %{version}-%{release}
Requires: PyYAML
Requires: attrs
Requires: decorator
Requires: docker
Requires: mxnet
Requires: numpy
Requires: onnx
Requires: python-graphviz
BuildRequires : PyYAML
BuildRequires : Vulkan-Headers-dev Vulkan-Loader-dev Vulkan-Tools
BuildRequires : attrs
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-cpan
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : buildreq-meson
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : decorator
BuildRequires : dmlc-core-dev
BuildRequires : docker
BuildRequires : doxygen
BuildRequires : eigen-data
BuildRequires : git
BuildRequires : glfw-dev
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : hwloc-dev
BuildRequires : llvm-dev
BuildRequires : mesa-dev
BuildRequires : mxnet
BuildRequires : numpy
BuildRequires : onnx
BuildRequires : openblas
BuildRequires : openblas-dev
BuildRequires : opencl-headers-dev
BuildRequires : opencv
BuildRequires : opencv-dev
BuildRequires : openjdk11-dev
BuildRequires : openssl-dev
BuildRequires : perl
BuildRequires : pkg-config
BuildRequires : pkgconfig(jemalloc)
BuildRequires : pkgconfig(libffi)
BuildRequires : protobuf-dev
BuildRequires : python-graphviz
BuildRequires : python3
BuildRequires : python3-dev
Patch1: 0001-Use-system-mkldnn.patch
Patch2: 0002-Use-system-dmlc-core.patch
Patch3: 0003-Put-.so-in-python-libdir.patch
Patch4: 0004-Unfreeze-graphviz.patch

%description
Apache MXNet (incubating) is a deep learning framework designed for both
efficiency and flexibility. It allows you to mix symbolic and imperative
programming to maximize efficiency and productivity. At its core, MXNet
contains a dynamic dependency scheduler that automatically parallelizes both
symbolic and imperative operations on the fly. A graph optimization layer on
top of that makes symbolic execution fast and memory efficient. MXNet is
portable and lightweight, scaling effectively to multiple GPUs and multiple
machines. MXNet is more than a deep learning project. It is a collection of
blue prints and guidelines for building deep learning systems, and interesting
insights of DL systems for hackers.

%package dev
Summary: dev components for the mxnet package.
Group: Development
Provides: mxnet-devel = %{version}-%{release}
Requires: mxnet = %{version}-%{release}

%description dev
dev components for the mxnet package.


%package license
Summary: license components for the mxnet package.
Group: Default

%description license
license components for the mxnet package.


%package python
Summary: python components for the mxnet package.
Group: Default
Requires: mxnet-python3 = %{version}-%{release}

%description python
python components for the mxnet package.


%package python3
Summary: python3 components for the mxnet package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mxnet package.


%prep
%setup -q -n apache-mxnet-src-1.6.0-incubating
cd %{_builddir}/apache-mxnet-src-1.6.0-incubating
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592970089
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DUSE_CUDA=OFF -DUSE_MKLDNN=0 -DUSE_BLAS=open
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1592970089
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mxnet
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/ctc_include/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/bc66df1f4263c0c4f2ed8b3a9ee8614bccf49b02
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/ctc_include/contrib/moderngpu/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/052c6a91d3037bf6488b6672aeec78374395c358
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/dlpack/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/b8180e52873e5515c764c336a1b07748da8c8ab0
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/dmlc-core/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/2a80cf3c998c66283de014c31b3df790c60625a1
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/googletest/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/googletest/googlemock/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/googletest/googlemock/scripts/generator/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/googletest/googletest/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/mkldnn/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/eebbd1242234444cdc8ddd5f0ee1f25069bde8ac
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/mkldnn/doc/assets/mathjax/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/mkldnn/src/cpu/jit_utils/jitprofiling/LICENSE.BSD %{buildroot}/usr/share/package-licenses/mxnet/be8f76850d5fd6458ff339a1a7df86bbec3e5366
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/mkldnn/src/cpu/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/mxnet/990f2a776789e9560c85fc1ddf2121d382223354
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/mkldnn/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/5a2314153eadadc69258a9429104cd11804ea304
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/mshadow/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/eda2b89df69e68e5e87e932fdfa33e9d17fd3922
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/nvidia_cub/LICENSE.TXT %{buildroot}/usr/share/package-licenses/mxnet/3e6ec0e8366114f809511fdbc4b94a1570204b1a
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/onnx-tensorrt/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/2093bd4f3f186c655497a3e5b0f969fed37e8227
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/onnx-tensorrt/third_party/onnx/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/e8438148b753bca339b6cc352f19cf4260806351
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/onnx-tensorrt/third_party/onnx/third_party/benchmark/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/onnx-tensorrt/third_party/onnx/third_party/pybind11/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/71a7f368f90789db807331860cb72d10abdb4acb
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/onnx-tensorrt/third_party/onnx/third_party/pybind11/tools/clang/LICENSE.TXT %{buildroot}/usr/share/package-licenses/mxnet/0ebae4fcb66d6688d40b27451ac84cf5b5c8862a
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/openmp/LICENSE.txt %{buildroot}/usr/share/package-licenses/mxnet/e3cccabb67bd491a643d32a7d2b65b49836e626d
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/ps-lite/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/6f4d766fd18fb785a6b8dabcd78ce3ad0f17dd42
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/tvm/3rdparty/dlpack/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/b8180e52873e5515c764c336a1b07748da8c8ab0
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/tvm/3rdparty/dmlc-core/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/2a80cf3c998c66283de014c31b3df790c60625a1
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/tvm/3rdparty/rang/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/24944bf7920108f5a4790e6071c32e9102760c37
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/3rdparty/tvm/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/contrib/clojure-package/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/9cf27e388af2632586cd49a7b5bc8bf93c0caeb9
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/cpp-package/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/2a80cf3c998c66283de014c31b3df790c60625a1
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/docs/python_docs/themes/mx-theme/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/7450be9140afa2a9e59db558320b671f103d50a3
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/example/gluon/tree_lstm/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/3b3274a4d15e949a12515588e9f46495f3729609
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/example/rcnn/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/d4f6bc536bf0b93250549871eaf4e0997274b605
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/julia/LICENSE.md %{buildroot}/usr/share/package-licenses/mxnet/d9e577d16a2a1f25b4cd0e65a3c97b44939bda9b
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/python/mxnet/contrib/onnx/mx2onnx/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/5a7a70a4faf7a46b3195f97c29d6493ad4d14ddb
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/scala-package/LICENSE %{buildroot}/usr/share/package-licenses/mxnet/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/apache-mxnet-src-1.6.0-incubating/tools/dependencies/LICENSE.binary.dependencies %{buildroot}/usr/share/package-licenses/mxnet/18be1a8bf0e2491fd6d41a712a677cc697095674
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/include/gtest/gtest-death-test.h
rm -f %{buildroot}/usr/include/gtest/gtest-message.h
rm -f %{buildroot}/usr/include/gtest/gtest-param-test.h
rm -f %{buildroot}/usr/include/gtest/gtest-param-test.h.pump
rm -f %{buildroot}/usr/include/gtest/gtest-printers.h
rm -f %{buildroot}/usr/include/gtest/gtest-spi.h
rm -f %{buildroot}/usr/include/gtest/gtest-test-part.h
rm -f %{buildroot}/usr/include/gtest/gtest-typed-test.h
rm -f %{buildroot}/usr/include/gtest/gtest.h
rm -f %{buildroot}/usr/include/gtest/gtest_pred_impl.h
rm -f %{buildroot}/usr/include/gtest/gtest_prod.h
rm -f %{buildroot}/usr/include/gtest/internal/custom/gtest-port.h
rm -f %{buildroot}/usr/include/gtest/internal/custom/gtest-printers.h
rm -f %{buildroot}/usr/include/gtest/internal/custom/gtest.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-death-test-internal.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-filepath.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-internal.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-linked_ptr.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-param-util-generated.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-param-util-generated.h.pump
rm -f %{buildroot}/usr/include/gtest/internal/gtest-param-util.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-port-arch.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-port.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-string.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-tuple.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-tuple.h.pump
rm -f %{buildroot}/usr/include/gtest/internal/gtest-type-util.h
rm -f %{buildroot}/usr/include/gtest/internal/gtest-type-util.h.pump
rm -f %{buildroot}/usr/include/omp.h
rm -f %{buildroot}/usr/lib/libgomp.so
rm -f %{buildroot}/usr/lib/libgtest.so
rm -f %{buildroot}/usr/lib/libgtest_main.so
rm -f %{buildroot}/usr/lib/libiomp5.so
rm -f %{buildroot}/usr/lib/libomp.so
## install_append content
pushd python
eu-strip $(pwd)/../clr-build/libmxnet.so
MXNET_LIBRARY_PATH=$(pwd)/../clr-build/libmxnet.so python3 -tt setup.py build install --root=%{buildroot}
popd
## install_append end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/dlpack/dlpack.h
/usr/include/mshadow/README.md
/usr/include/mshadow/base.h
/usr/include/mshadow/cuda/reduce.cuh
/usr/include/mshadow/cuda/tensor_gpu-inl.cuh
/usr/include/mshadow/dot_engine-inl.h
/usr/include/mshadow/expr_engine-inl.h
/usr/include/mshadow/expr_scalar-inl.h
/usr/include/mshadow/expression.h
/usr/include/mshadow/extension.h
/usr/include/mshadow/extension/broadcast.h
/usr/include/mshadow/extension/broadcast_with_axis.h
/usr/include/mshadow/extension/channel_pool.h
/usr/include/mshadow/extension/channel_unpool.h
/usr/include/mshadow/extension/choose.h
/usr/include/mshadow/extension/complex.h
/usr/include/mshadow/extension/concat.h
/usr/include/mshadow/extension/crop.h
/usr/include/mshadow/extension/fill.h
/usr/include/mshadow/extension/flip.h
/usr/include/mshadow/extension/implicit_gemm.h
/usr/include/mshadow/extension/mask.h
/usr/include/mshadow/extension/mirror.h
/usr/include/mshadow/extension/one_hot.h
/usr/include/mshadow/extension/pack_col2patch.h
/usr/include/mshadow/extension/pad.h
/usr/include/mshadow/extension/range.h
/usr/include/mshadow/extension/reduce_with_axis.h
/usr/include/mshadow/extension/reduceto1d.h
/usr/include/mshadow/extension/reshape.h
/usr/include/mshadow/extension/slice.h
/usr/include/mshadow/extension/slice_ex.h
/usr/include/mshadow/extension/spatial_pool.h
/usr/include/mshadow/extension/spatial_unpool.h
/usr/include/mshadow/extension/spatial_upsampling_nearest.h
/usr/include/mshadow/extension/swapaxis.h
/usr/include/mshadow/extension/take.h
/usr/include/mshadow/extension/take_grad.h
/usr/include/mshadow/extension/transpose.h
/usr/include/mshadow/extension/unpack_patch2col.h
/usr/include/mshadow/half.h
/usr/include/mshadow/half2.h
/usr/include/mshadow/io.h
/usr/include/mshadow/logging.h
/usr/include/mshadow/packet-inl.h
/usr/include/mshadow/packet/plain-inl.h
/usr/include/mshadow/packet/sse-inl.h
/usr/include/mshadow/random.h
/usr/include/mshadow/stream_gpu-inl.h
/usr/include/mshadow/tensor.h
/usr/include/mshadow/tensor_container.h
/usr/include/mshadow/tensor_cpu-inl.h
/usr/include/mshadow/tensor_gpu-inl.h
/usr/include/mxnet/base.h
/usr/include/mxnet/c_api.h
/usr/include/mxnet/c_api_error.h
/usr/include/mxnet/c_api_test.h
/usr/include/mxnet/c_predict_api.h
/usr/include/mxnet/engine.h
/usr/include/mxnet/executor.h
/usr/include/mxnet/graph_attr_types.h
/usr/include/mxnet/imperative.h
/usr/include/mxnet/io.h
/usr/include/mxnet/kvstore.h
/usr/include/mxnet/lib_api.h
/usr/include/mxnet/libinfo.h
/usr/include/mxnet/ndarray.h
/usr/include/mxnet/op_attr_types.h
/usr/include/mxnet/operator.h
/usr/include/mxnet/operator_util.h
/usr/include/mxnet/random_generator.h
/usr/include/mxnet/resource.h
/usr/include/mxnet/rtc.h
/usr/include/mxnet/storage.h
/usr/include/mxnet/tensor_blob.h
/usr/include/mxnet/tuple.h
/usr/include/nnvm/base.h
/usr/include/nnvm/c_api.h
/usr/include/nnvm/compiler/op_attr_types.h
/usr/include/nnvm/compiler/packed_func_ext.h
/usr/include/nnvm/compiler/util.h
/usr/include/nnvm/graph.h
/usr/include/nnvm/graph_attr_types.h
/usr/include/nnvm/layout.h
/usr/include/nnvm/node.h
/usr/include/nnvm/op.h
/usr/include/nnvm/op_attr_types.h
/usr/include/nnvm/pass.h
/usr/include/nnvm/pass_functions.h
/usr/include/nnvm/symbolic.h
/usr/include/nnvm/top/README
/usr/include/nnvm/top/nn.h
/usr/include/nnvm/top/tensor.h
/usr/include/nnvm/tuple.h
/usr/include/omp-tools.h
/usr/include/ompt.h
/usr/lib64/libmxnet.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mxnet/052c6a91d3037bf6488b6672aeec78374395c358
/usr/share/package-licenses/mxnet/0ebae4fcb66d6688d40b27451ac84cf5b5c8862a
/usr/share/package-licenses/mxnet/18be1a8bf0e2491fd6d41a712a677cc697095674
/usr/share/package-licenses/mxnet/1d4719e04eaa4909ab5a59ef5cb04d2a5517716e
/usr/share/package-licenses/mxnet/2093bd4f3f186c655497a3e5b0f969fed37e8227
/usr/share/package-licenses/mxnet/24944bf7920108f5a4790e6071c32e9102760c37
/usr/share/package-licenses/mxnet/2a80cf3c998c66283de014c31b3df790c60625a1
/usr/share/package-licenses/mxnet/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/mxnet/3b3274a4d15e949a12515588e9f46495f3729609
/usr/share/package-licenses/mxnet/3e6ec0e8366114f809511fdbc4b94a1570204b1a
/usr/share/package-licenses/mxnet/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/mxnet/5a7a70a4faf7a46b3195f97c29d6493ad4d14ddb
/usr/share/package-licenses/mxnet/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/mxnet/6f4d766fd18fb785a6b8dabcd78ce3ad0f17dd42
/usr/share/package-licenses/mxnet/71a7f368f90789db807331860cb72d10abdb4acb
/usr/share/package-licenses/mxnet/7450be9140afa2a9e59db558320b671f103d50a3
/usr/share/package-licenses/mxnet/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/mxnet/990f2a776789e9560c85fc1ddf2121d382223354
/usr/share/package-licenses/mxnet/9cf27e388af2632586cd49a7b5bc8bf93c0caeb9
/usr/share/package-licenses/mxnet/b8180e52873e5515c764c336a1b07748da8c8ab0
/usr/share/package-licenses/mxnet/bc66df1f4263c0c4f2ed8b3a9ee8614bccf49b02
/usr/share/package-licenses/mxnet/be8f76850d5fd6458ff339a1a7df86bbec3e5366
/usr/share/package-licenses/mxnet/d4f6bc536bf0b93250549871eaf4e0997274b605
/usr/share/package-licenses/mxnet/d9e577d16a2a1f25b4cd0e65a3c97b44939bda9b
/usr/share/package-licenses/mxnet/e3cccabb67bd491a643d32a7d2b65b49836e626d
/usr/share/package-licenses/mxnet/e8438148b753bca339b6cc352f19cf4260806351
/usr/share/package-licenses/mxnet/eda2b89df69e68e5e87e932fdfa33e9d17fd3922
/usr/share/package-licenses/mxnet/eebbd1242234444cdc8ddd5f0ee1f25069bde8ac

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
