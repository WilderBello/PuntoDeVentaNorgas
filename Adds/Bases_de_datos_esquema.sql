create table Credenciales(
    id integer PRIMARY KEY autoincrement,
    correo varchar(50) UNIQUE NOT NULL,
    password varchar NOT NULL,
    username varchar(50) NOT NULL
);
create table BaseDeDatos (
    id_cliente varchar(20) PRIMARY KEY NOT NULL,
    nombre_completo varchar(100) NOT NULL,
    telefono varchar(100) NOT NULL,
    direccion varchar(100) NOT NULL,
    fecha_registro date NOT NULL,
    referencia_producto varchar(100) NOT NULL,
    num_producto int NOT NULL,
    estado_producto boolean NOT NULL,
    deuda float NOT NULL,
    anotaciones varchar(200),
    id_departamento int NOT NULL,
    telefono_departamento varchar(100) NOT NULL,
    id_pedido integer NOT NULL,
    fecha_pedido date NOT NULL,
    foreign key (id_pedido) references Pedido (id_pedido_now)
);
create table Cliente (
    id_cli varchar(20) PRIMARY KEY NOT NULL,
    nombre_cli varchar(100) NOT NULL,
    telefono_cli varchar(100) NOT NULL,
    direccion_cli varchar(100) NOT NULL
);
create table Empresa (
    id_nit varchar(50) PRIMARY KEY NOT NULL,
    nombre_empresa varchar(100) NOT NULL,
    telefono_empresa varchar(100) NOT NULL,
    num_empleados int NOT NULL
);
create table Producto (
    referencia_producto varchar(100) PRIMARY KEY NOT NULL,
    num_productos int NOT NULL,
    precio int NOT NULL
);
create table Pedido (
    id_pedido_now integer PRIMARY KEY autoincrement,
    fecha_pedido_now date NOT NULL,
    referencia_producto varchar(100) NOT NULL,
    foreign key (referencia_producto) references Producto (referencia_producto)
);
-- drop table Pedido;
create table Venta (
    id_emp varchar(50) NOT NULL,
    id_departamento int PRIMARY KEY NOT NULL,
    telefono_departamento varchar(100) NOT NULL,
    cc_cli_ped varchar(20) NOT NULL, 
    foreign key (cc_cli_ped) references Cliente (id_cli),
    foreign key (id_emp) references Empresa (id_nit)
);
-- drop table Venta;
create table Ventaxpedido (
    id_dep_ped int not null,
    id_ped_ped int not null,
    foreign key (id_dep_ped) references Venta (id_departamento),
    foreign key (id_ped_ped) references Pedido (id_pedido_now)
);
-- drop table Ventaxpedido;
create table Pedidoxarticulo (
    ref_artped varchar(100) NOT NULL,
    id_ped_artped int NOT NULL,
    cant_art_ped int NOT NULL,
    val_venta_art_ped float NOT NULL,
    foreign key (ref_artped) references Producto (referencia_producto),
    foreign key (id_ped_artped) references Pedido (id_pedido_now)
);
-- drop table Pedidoxarticulo;
