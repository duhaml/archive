
import { createStackNavigator, createDrawerNavigator, createAppContainer } from 'react-navigation'
import HomePage from '../Components/HomePage'
import CreateAccount from '../Components/CreateAccount'
import Tutorial from '../Components/Tutorial'
import GlobalMarketView from '../Components/GlobalMarketView'
import Login from '../Components/Login'
import Settings from '../Components/Settings'
import Needs from '../Components/Needs'
import MyAccount from '../Components/MyAccount'

const MyDrawerNavigator = createDrawerNavigator({
  "Mon Compte": {
    screen: MyAccount
  },
  "Les Offres": {
    screen: GlobalMarketView
  },
  "Les Demandes": {
    screen: Needs
  },
  "Paramètres":{
    screen: Settings
  }
})

const MyStackNavigator = createStackNavigator({
  HomePage: { 
    screen: HomePage,
    navigationOptions: {
      title: 'HomePage'
    }
  },
  CreateAccount: { 
    screen: CreateAccount
  },
  Tutorial:{
    screen: Tutorial
  },
  GlobalMarketView:{
    screen: MyDrawerNavigator
  },
  Login:{
    screen: Login
  }
})


export default createAppContainer(MyStackNavigator)