import logo from './logo.svg';
import './App.css';
import Productos from './componentes/Productos';
import Producto from './componentes/Producto';
import Layout from './componentes/Layout';
import Title from './componentes/Title';
import Navbar from './componentes/Navbar';

constructor(props) {
  super(props);
  this.state = {
    productos: [],
    carro:[],
    esCarroVisible: false
  };
}

componentDidMount() {
  fetch('http://localhost:8000/productos')
    .then((response) => {
      return response.json()
    })
    .then((prod) => {
      this.setState({ productos: prod })
    })    
} 

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}
agregarAlCarro = (producto) => {
  const { carro } = this.state
  if(carro.find(x => x.nombre === producto.nombre)) {
    const newCarro = carro.map(x => x.nombre === producto.nombre
      ? ({
        ...x,
        cantidad: x.cantidad + 1
      })
      : x)
    return this.setState({carro: newCarro})
  }
  return this.setState({
    carro: this.state.carro.concat({
      ...producto,
      cantidad: 1,
    })
  })
}

mostrarCarro = () => {
  if(!this.state.carro.length){
    return
  }
  this.setState({esCarroVisible: !this.state.esCarroVisible})
}

render() {
  const {esCarroVisible} = this.state
  return (
    <div>
      <Navbar carro={this.state.carro} 
      esCarroVisible={esCarroVisible} 
      mostrarCarro={this.mostrarCarro}/>
      <Layout>
        <Title/>
        <Productos
          agregarAlCarro={this.agregarAlCarro}
          productos={this.state.productos}
        />
      </Layout>
    </div>
  )  
}

export default App;
