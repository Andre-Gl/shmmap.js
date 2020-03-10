#include <nan.h>
#include <node.h>

NAN_METHOD(open) {}

NAN_METHOD(resize) {}

NAN_METHOD(unlink) {}

NAN_MODULE_INIT(Init) {
  NAN_EXPORT(target, open);
  NAN_EXPORT(target, resize);
  NAN_EXPORT(target, unlink);
}

NODE_MODULE(shmmap, Init)
