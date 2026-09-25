FROM golang:alpine AS builder
WORKDIR /build
COPY ./simplehttp.go .
RUN go build -o simplehttp ./simplehttp.go
WORKDIR /dist
RUN cp /build/simplehttp .
EXPOSE 8080

FROM scratch
COPY --from=builder /dist/simplehttp /
ENTRYPOINT [ "/simplehttp" ]