import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import HomePage from '../MyCampusMarket/Components/HomePage'
import Navigation from '../MyCampusMarket/Navigation/Navigation'
import CreateAccount from './Components/CreateAccount';
import Tutorial from './Components/Tutorial';
import GlobalMarketView from './Components/GlobalMarketView';
import Login from './Components/Login';
import Needs from './Components/Needs';


export default class App extends React.Component {
  render() {
    return (
      <Navigation/>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
